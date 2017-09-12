"""Various classes that manage local CSV files."""
import os
from apps.helpers.repository import get_parent_repo_url, download_file_contents

class LocalFile(object):
    """Class that controls a local CSV file."""
    def __init__(self, filename, dirname='files'):
        self.path = os.path.join(dirname, filename)
        self.url = get_parent_repo_url(filename)

    def __eq__(self, x):
        return self.get_contents() == x.get_contents()

    def update_from_parent_repo(self):
        """Update a local copy with the latest content from the main
           GitHub repository.
        """
        data = download_file_contents(self.url)
        with open(self.path, 'w') as csv:
            csv.write(data)

    def get_contents(self):
        """Return contents of a local copy."""
        with open(self.path, 'r') as csv:
            contents = csv.read()
        return contents
