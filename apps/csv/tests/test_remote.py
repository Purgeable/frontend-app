import unittest

from apps import app
from apps.csv.remote import RemoteFile

class RemoveFileTestCase(unittest.TestCase):
    def setUp(self):
        self.csv = RemoteFile('dfm.csv')

    def test_attrs(self):
        assert self.csv.url == f"{app.config['REMOTE_CSV_URL']}/dfm.csv"
