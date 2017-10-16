Macroeconomic datafeed
======================

Github: <https://github.com/mini-kep/frontend-app>

Changelog
=========

**2017-09-07:** Custom API relays time series from [db](https://github.com/mini-kep/db). 

Sample calls (CSV files):

- <http://mini-kep.herokuapp.com/oil/series/BRENT/d/2017/>
- <http://mini-kep.herokuapp.com/ru/series/USDRUR_CB/d/2017/>
- <http://mini-kep.herokuapp.com/ru/series/CPI_rog/m/2000/2010>
- <http://mini-kep.herokuapp.com/ru/series/CPI/m/rog/2000/2010>
- <http://mini-kep.herokuapp.com/ru/series/GDP/a/yoy/1998/2017>

Sample use:
```python
import pandas as pd

def read_ts(source_url):
    """Read pandas time series from *source_url*"""
    df = pd.read_csv(source_url, converters={0: pd.to_datetime}, index_col=0)
    return df.iloc[:,0] 

usd_er = read_ts('http://mini-kep.herokuapp.com/ru/series/USDRUR_CB/d/2017/')

assert usd_er['2017-09-28'] == 58.01022

```


**2017-09-07:** This app has three URLs that relay annual, quarterly and monthly macroeconomic time series
from [mini-kep parser](https://github.com/epogrebnyak/mini-kep).


You can get this data with [pandas](http://pandas.pydata.org/pandas-docs/stable/install.html) using code below:

```python
import pandas as pd

URL = {'a': 'http://mini-kep.herokuapp.com/annual',
    'q': 'http://mini-kep.herokuapp.com/quarterly',
    'm': 'http://mini-kep.herokuapp.com/monthly'}

def read_csv(source):
    return pd.read_csv(source, converters={0: pd.to_datetime}, index_col=0)

dfa, dfq, dfm = (read_csv(URL[freq]) for freq in 'aqm')
```
