import unittest
import config

from apps.csv.remote import RemoteFile
from apps.helpers.repository import get_parent_repo_url, download_file_contents

class RepositoryTestCase(unittest.TestCase):
    def test_get_parent_repo_url(self):
        url = get_parent_repo_url('dfa.csv')
        assert isinstance(url, str)
        data = RemoteFile(url).get_contents()
        assert isinstance(data, str)
        assert data

    def test_download_file_contents(self):
        data = download_file_contents(f"{config.REMOTE_CSV_URL}/dfm.csv")
        assert isinstance(data, str)
        assert data
