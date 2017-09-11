"""Helper functions that work with GitHub repositories."""
from apps import app
from urllib import request

def get_parent_repo_url(filename):
    """Return full URL path in a remote repository to the specified CSV
    file.
    """
    return f"{app.config['REMOTE_CSV_URL']}/{filename}"

def download_file_contents(url):
    """Return UTF8-encoded file contents from a remote CSV file."""
    return request.urlopen(url).read().decode('utf-8')
