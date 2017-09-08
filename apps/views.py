import json
import datetime
import subprocess
#import markdown2 as md

from flask import (Blueprint, render_template_string, render_template,
                   jsonify, Markup)
from .classes import LocalFile, RemoteFile

# Define the blueprint for this application
main = Blueprint('main', __name__, template_folder='../templates')

@main.route('/')
def home():
    #FIXME: maybe pygments can go here too?
    md_extras = ['fenced-code-blocks']
    source = render_template('home.html')
    contents = Markup(md.markdown(source, extras=md_extras))
    return render_template_string(contents)

def render_file(filename):
    csv_file = LocalFile(filename)
    contents = csv_file.get_contents()
    return render_template_string(contents)

@main.route('/annual/')
def annual():
    return render_file('dfa.csv')

@main.route('/quarterly/')
def quarterly():
    return render_file('dfq.csv')

@main.route('/monthly/')
def monthly():
    return render_file('dfmq.csv')

@main.route('/status/')
def check_status():
    with open('status.json') as f:
        json_data = json.loads(f.read())
    return jsonify(json_data)

# Not used - to depreciate ----------------------------------------------------                
class ExitCodeDoesNotExist(Exception):
    """Raise when pytest exit code is unknown."""
    pass


def get_pytest_integration_test_result():  
    """Return pytest result and string comment."""
    comments = {
        0: "All tests were collected and passed successfully",
        1: "Tests were collected and run but some of the tests failed",
        2: "Test execution was interrupted by the user",
        3: "Internal error happened while executing tests",
        4: "pytest command line usage error",
        5: "No tests were collected"
    }
    # not this specific to integration test
    exit_code = subprocess.call(['pytest'], shell=True)
    try:
         return exit_code, comments[exit_code]
    except KeyError:
         raise ExitCodeDoesNotExist("pytest exited with an unknown code")   
 # end  -----------------------------------------------------------------------
  
def check_csv_identity(): 
    flags = []
    for filename in ['dfa.csv', 'dfq.csv', 'dfm.csv']:
        # this will use get_contents()
        flag = (LocalFile(filename) == RemoteFile(filename))
        flags.append(flag)
    return all(flags)
  
def from_json(filename):
    with open(filename, 'r') as f:
        content = f.read()
    return json.loads(content)
    
def to_json(what, filename):
    # Save test results to status.json
    with open(filename, 'w') as f:
        content = json.dumps(what)
        f.write(content)        
    

@main.route('/webhook/', methods=['POST'])
def webhook():
    """Receive payload from GitHub webhook and re-check file identity."""
   
    #EP: we had to update files first before test! Not after it! ;))
    
    # Update local copies with the latest data
    filenames = ['dfa.csv', 'dfm.csv', 'dfq.csv']
    for name in filenames:
        csv_file = LocalFile(name)
        csv_file.update_from_parent_repo()
    
    # get a bool on identity of the files
    is_updated_ok = check_csv_identity()    
    
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    status_dict = {'timestamp': now,
                   'is_updated_ok': is_updated_ok}
    to_json(status_dict, 'status.json')

    return render_template_string("")
