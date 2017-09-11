import unittest
import config

from apps.csv.remote import RemoteFile

class RemoveFileTestCase(unittest.TestCase):
    def setUp(self):
        self.csv = RemoteFile('dfm.csv')

    def test_attrs(self):
        assert self.csv.url == f"{config.REMOTE_CSV_URL}/dfm.csv"
