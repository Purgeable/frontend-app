import os
import unittest
import pandas as pd
import config

from apps import app
from apps.csv.local import LocalFile

class LocalFileTestCase(unittest.TestCase):
    def setUp(self):
        self.csv = LocalFile('dfa.csv')

    def test_attrs(self):
        assert os.path.exists(self.csv.path)
        ds_conf = config.DataSourceConfig
        assert self.csv.url == f"{ds_conf.BASE_URL}/{ds_conf.CSV_FILES[0]}"

    def test_update_from_parent_repo(self):
        self.csv.update_from_parent_repo()
        contents = pd.read_csv(self.csv.url, converters={0: pd.to_datetime},
                               index_col=0)
        assert not contents.empty

    def test_get_contents(self):
        contents = self.csv.get_contents()
        assert isinstance(contents, str)
