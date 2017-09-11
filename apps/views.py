import datetime

from flask import Blueprint, render_template_string, jsonify
from apps.csv.local import LocalFile
from apps.csv.remote import RemoteFile
from apps.decorators import with_markdown
from apps.helpers.json import to_json, from_json

# Define module constants
FILENAMES = ('dfa.csv', 'dfq.csv', 'dfm.csv')

# Define the blueprint for this application
main = Blueprint('main', __name__)

@main.route('/')
@with_markdown('home.md')
def home():
    pass

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
    return render_file('dfm.csv')

def check_csv_identity():
    """Ensure that contents of local CSV files match their remote
    counterparts.
    """
    flags = []
    for filename in FILENAMES:
        # this will use get_contents()
        flag = (LocalFile(filename) == RemoteFile(filename))
        flags.append(flag)
    return all(flags)

@main.route('/status/')
def check_status():
    """Page that reflects the current status of file identity."""
    return jsonify(from_json('status.json'))

@main.route('/webhook/', methods=['POST'])
def webhook():
    """Receive payload from GitHub webhook and re-check file identity."""
    # Update local copies with the latest data
    for name in FILENAMES:
        csv_file = LocalFile(name)
        csv_file.update_from_parent_repo()

    # get a bool on identity of the files
    is_updated_ok = check_csv_identity()

    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    status_dict = {
        'timestamp': now,
        'is_updated_ok': is_updated_ok
    }
    to_json(status_dict, 'status.json')
    return render_template_string("")
