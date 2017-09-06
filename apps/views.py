import json
import datetime
import subprocess

from flask import Blueprint, render_template_string, render_template, \
                  request, jsonify
from .classes import CSVFile
from .df_string_proxies import dfa_text, dfm_text, dfq_text

# Define the blueprint for this application
main = Blueprint('main', __name__, template_folder='../templates')

@main.route('/')
def home():
    return render_template('home.html')

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

@main.route('/webhook/', methods=['GET'])
def webhook():
    """Receive payload from GitHub webhook then run tests."""
    def _get_comment_from_exitcode(code):
        if code == 0:
            return "All tests were collected and passed successfully"
        if code == 1:
            return "Tests were collected and run but some of the tests failed"
        if code == 2:
            return "Test execution was interrupted by the user"
        if code == 3:
            return "Internal error happened while executing tests"
        if code == 4:
            return "pytest command line usage error"
        if code == 5:
            return "No tests were collected"

    json_data = request.get_json()
    exit_code = subprocess.call(['pytest'], shell=True)
    with open('status.json', 'w') as f:
        comment = _get_comment_from_exitcode(exit_code)
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        body = {
            'timestamp': now,
            'pytest_exit_code': exit_code,
            'is_validated': exit_code == 0,
            'comment': comment
        }
        f.write(json.dumps(body))
        f.close()

    # Update local copies with the latest data
    filenames = ['dfa.csv', 'dfm.csv', 'dfq.csv']
    for name in filenames:
        csv_file = CSVFile(name)
        csv_file.update()
    return render_template_string("")
