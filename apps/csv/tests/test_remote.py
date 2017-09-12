import unittest
import config

from apps import app
from apps.csv.remote import RemoteFile

class RemoveFileTestCase(unittest.TestCase):
    def setUp(self):
        self.csv = RemoteFile('dfa.csv')

    def test_attrs(self):
        ds_conf = config.DataSourceConfig
        assert self.csv.url == f"{ds_conf.BASE_URL}/{ds_conf.CSV_FILES[0]}"
