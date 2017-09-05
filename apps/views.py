import json
import datetime
import subprocess

from flask import Blueprint, render_template_string, request, jsonify
from .df_string_proxies import dfa_text, dfm_text, dfq_text

# Define the blueprint for this application
main = Blueprint('main', __name__)

@main.route('/annual/')
def annual():
    content = dfa_text
    return render_template_string(content)

@main.route('/quarterly/')
def quarterly():
    content = dfq_text
    return render_template_string(content)

@main.route('/monthly/')
def monthly():
    content = dfm_text
    return render_template_string(content)

@main.route('/status/')
def check_status():
    with open('status.json') as f:
        json_data = json.loads(f.read())
        f.close()
    return jsonify(json_data)

@main.route('/webhook/', methods=['POST'])
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
        body = '{"timestamp": "%s", "status": %s, "comment": "%s"}' % (
            now,
            exit_code,
            comment
        )
        f.write(body)
        f.close()
    return render_template_string("")
