import os
from urllib import request


def get_parent_repo_url(filename):
    url = "https://raw.githubusercontent.com/epogrebnyak/mini-kep/master/data/processed/latest/{}"
    return url.format(filename) 

def download_file_contents(url):
    return request.urlopen(url).read().decode('utf-8')
    

class LocalFile(object):
    """Class that controls a local CSV file."""
    def __init__(self, filename, dirname='files'):
        self.path = os.path.join(dirname, filename)
        self.url = get_parent_repo_url(filename)            

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
    
    def __eq__(self, x):
        return self.get_contents() == x.get_contents()

class RemoteFile(object):
    """Class that controls a local CSV file."""
    def __init__(self, filename):
        self.url = get_parent_repo_url(filename)

    def get_contents(self):
        """Return contents of a remote file."""
        return download_file_contents(self.url)    
