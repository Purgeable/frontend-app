from flask import Blueprint, render_template_string, request
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

@main.route('/webhook/', methods=['POST'])
def webhook():
    """Receive payload from GitHub webhook then run tests."""
    json_data = request.get_json()
    raise Exception("RECEIVED", json_data)
