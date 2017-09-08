import json
import datetime
import subprocess
import markdown2 as md

from flask import Blueprint, render_template_string, render_template, \
                  jsonify, Markup
from .classes import CSVFile

# Define the blueprint for this application
main = Blueprint('main', __name__, template_folder='../templates')

@main.route('/')
def home():
    md_extras = ['fenced-code-blocks']
    source = render_template('home.html')
    contents = Markup(md.markdown(source, extras=md_extras))
    return render_template_string(contents)

@main.route('/annual/')
def annual():
    csv_file = CSVFile('dfa.csv')
    contents = csv_file.get_contents()
    return render_template_string(contents)

@main.route('/quarterly/')
def quarterly():
    csv_file = CSVFile('dfq.csv')
    contents = csv_file.get_contents()
    return render_template_string(contents)

@main.route('/monthly/')
def monthly():
    csv_file = CSVFile('dfm.csv')
    contents = csv_file.get_contents()
    return render_template_string(contents)

@main.route('/status/')
def check_status():
    with open('status.json') as f:
        json_data = json.loads(f.read())
        f.close()
    return jsonify(json_data)

class ExitCodeDoesNotExist(Exception):
    """Raise when pytest exit code is unknown."""
    pass

@main.route('/webhook/', methods=['POST'])
def webhook():
    """Receive payload from GitHub webhook then run tests."""
    comments = {
        0: "All tests were collected and passed successfully",
        1: "Tests were collected and run but some of the tests failed",
        2: "Test execution was interrupted by the user",
        3: "Internal error happened while executing tests",
        4: "pytest command line usage error",
        5: "No tests were collected"
    }
    exit_code = subprocess.call(['pytest'], shell=True)

    # Save test results to status.json
    with open('status.json', 'w') as json_file:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        try:
            comment = comments[exit_code]
        except KeyError:
            raise ExitCodeDoesNotExist("pytest exited with an unknown code")
        body = {
            'timestamp': now,
            'pytest_exit_code': exit_code,
            'is_validated': exit_code == 0,
            'comment': comment
        }
        json_file.write(json.dumps(body))
        json_file.close()

    # Update local copies with the latest data
    filenames = ['dfa.csv', 'dfm.csv', 'dfq.csv']
    for name in filenames:
        csv_file = CSVFile(name)
        csv_file.update()
    return render_template_string("")
