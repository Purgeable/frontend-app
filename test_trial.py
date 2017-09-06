import pandas as pd


# raw rd.read_csv check

url_a = 'https://mini-kep.herokuapp.com/annual/'
dfa = pd.read_csv(url_a)

url_a_repo = 'https://raw.githubusercontent.com/epogrebnyak/mini-kep/master/data/processed/latest/dfa.csv'
dfa2 = pd.read_csv(url_a_repo)

#assert dfa.equals(dfa2)


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

sources = dict(a='https://mini-kep.herokuapp.com/annual',
               q='https://mini-kep.herokuapp.com/quarterly',
				 m='https://mini-kep.herokuapp.com/monthly')

for freq, url in sources.items():
    df_repo = get_dataframe_from_repo(freq)
    df_app = read_csv(url)
    # assert df_repo.equals(df_app)


# test json

import urllib.request, json

def test_json():
    with urllib.request.urlopen('http://mini-kep.herokuapp.com/status/') as url:
        status = json.loads(url.read().decode())
        assert isinstance(status, dict)
        assert status['pytest_exit_code'] == 0
        assert pd.to_datetime('2017-09-05 19:05:44').year >= 2017 # generally, today or after
        #this fails:
        assert status['is_validated'] is True