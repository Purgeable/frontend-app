import os
import unittest
import pandas as pd

from apps import app
from apps.csv.local import LocalFile

class LocalFileTestCase(unittest.TestCase):
    def setUp(self):
        self.csv = LocalFile('dfa.csv')

    def test_attrs(self):
        assert os.path.exists(self.csv.path)
        assert self.csv.url == f"{app.config['REMOTE_CSV_URL']}/dfa.csv"

    def test_update_from_parent_repo(self):
        self.csv.update_from_parent_repo()
        contents = pd.read_csv(self.csv.url, converters={0: pd.to_datetime},
                               index_col=0)
        assert not contents.empty

    def test_get_contents(self):
        contents = self.csv.get_contents()
        assert isinstance(contents, str)
