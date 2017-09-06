import json
import urllib.request
import pandas as pd

from datetime import date

BASE_URL = 'https://mini-kep.herokuapp.com/'

# client reader check

def read_csv(source):
    """Canonical wrapper for pd.read_csv().

       Treats first column at time index.

       Retruns:
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

def test_csv_integrity():
    sources = {
        'a': '%sannual' % BASE_URL,
        'q': '%squarterly' % BASE_URL,
        'm': '%smonthly' % BASE_URL
    }
    for freq, url in sources.items():
        df_repo = get_dataframe_from_repo(freq)
        df_app = read_csv(url)
        assert df_repo.equals(df_app)

def test_status_json():
    with urllib.request.urlopen('%sstatus/' % BASE_URL) as url:
        status = json.loads(url.read().decode())
        assert isinstance(status, dict)
        assert status['pytest_exit_code'] == 0
        current_year = date.today().year
        year = pd.to_datetime(status['timestamp']).year
        assert year >= current_year # generally, today or after
        assert status['is_validated'] is True
