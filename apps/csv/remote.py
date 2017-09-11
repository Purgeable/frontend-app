"""Various classes that manage remote CSV files."""
from apps.helpers.repository import get_parent_repo_url, download_file_contents

class RemoteFile(object):
    """Class that controls a remote CSV file."""
    def __init__(self, filename):
        self.url = get_parent_repo_url(filename)

    def get_contents(self):
        """Return contents of a remote file."""
        return download_file_contents(self.url)
