import json
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
    json_data = request.get_json()
    exit_code = subprocess.call(['pytest'], shell=True)
    with open('status.json', 'w') as f:
        status = 'success' if exit_code == 0 else 'error'
        f.write('{"status": "%s"}' % status)
        f.close()
    return render_template_string("")
