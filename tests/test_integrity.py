import json
import urllib.request
import unittest
import pandas as pd
import config

from datetime import date

def read_csv(source):
    """Canonical wrapper for pd.read_csv().

       Treats first column at time index.

       Returns:
           pd.DataFrame()
    """
    converter_arg = dict(converters={0: pd.to_datetime}, index_col=0)
    return pd.read_csv(source, **converter_arg)

def make_url(freq):
    url_base = "https://raw.githubusercontent.com/epogrebnyak/mini-kep/master/data/processed/latest/{}"
    filename = "df{}.csv".format(freq)
    return url_base.format(filename)

def get_dataframe_from_repo(freq):
    """Suggested code to read pandas dataframes from 'mini-kep' stable URL."""
    url = make_url(freq)
    return read_csv(url)

class IntegrityTestCase(unittest.TestCase):
    def test_integrity(self):
        sources = {
            'a': '%sannual' % config.BASE_URL,
            'q': '%squarterly' % config.BASE_URL,
            'm': '%smonthly' % config.BASE_URL
        }
        for freq, url in sources.items():
            df_repo = get_dataframe_from_repo(freq)
            df_app = read_csv(url)
            assert df_repo.equals(df_app)

    def test_status_json(self):
        with urllib.request.urlopen('%sstatus/' % config.BASE_URL) as url:
            status = json.loads(url.read().decode())
            assert isinstance(status, dict)
            assert status['pytest_exit_code'] == 0
            current_year = date.today().year
            year = pd.to_datetime(status['timestamp']).year
            assert year >= current_year # generally, today or after
            assert status['is_validated'] is True
