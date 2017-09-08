[![Build Status](https://travis-ci.org/epogrebnyak/mini-kep-app.svg?branch=master)](https://travis-ci.org/epogrebnyak/mini-kep-app)

# mini-kep-app
Flask app with API to get macroeconomic time series

## v.0.1 - relay three CSVs by github webhook + intro at frontpage

#### App address:

   - <http://mini-kep.herokuapp.com>

#### Frontpage: 
  - has code exmaple
  - renders markdown
  - [some generic css theme + pygments](https://github.com/epogrebnyak/mini-kep-app/issues/4)?

#### Data interfaces:

   - <http://mini-kep.herokuapp.com/annual>
   - <http://mini-kep.herokuapp.com/quarterly>
   - <http://mini-kep.herokuapp.com/monthly>
   
   
Data interfaces relay copies of the following files: 
- [dfa.csv](https://raw.githubusercontent.com/epogrebnyak/mini-kep/master/data/processed/latest/dfa.csv), 
- [dfq.csv](https://raw.githubusercontent.com/epogrebnyak/mini-kep/master/data/processed/latest/dfq.csv), 
- [dfm.csv](https://raw.githubusercontent.com/epogrebnyak/mini-kep/master/data/processed/latest/dfm.csv).

#### Github webhook:

   On ```issue_comment``` or ```release```  three CSV files are updated in app.

#### Status URL:

<http://mini-kep.herokuapp.com/status> provides json with latest repo-app data syncronisation status. 


#### Integration test:
 
The logic of [the test](https://github.com/epogrebnyak/mini-kep-app/blob/master/tests/test_integrity.py)
is assure identity of the csv files at parent repo ant and app data interfaces.

## Proposed enhancements: 

- see listing at <https://github.com/epogrebnyak/mini-kep-app/issues/1>

- custom domain/URL

- requests log to catch popular series: <https://fred.stlouisfed.org/#popular-series>

- url for the list of variable names ```<app>/names```
  - needs a list of these names to be created in repo (not done yet)
  - also nice to organise it by section 
  - the sections can be used to list variables on frontpage

- put *here is the latest data* on frontpage
  - can prototype it at mini-kep README.md 
  - depends on <https://github.com/epogrebnyak/mini-kep/issues/78>
  
- interface to get specific variables, not just all dataframe 

```python
get_ts('m', 'CPI_rog') #  just one variable by varname
get_group('q', 'CPI')  #  variables starting with CPI*
get_df('a', ['CPI_rog', 'RETAIL_SALES_rog', 'SOC_WAGE_rog']) # several variables by names

# maybe this should be a call to like:
get(freq, vars)
# where *vars* may be a string or a list of varname(s) and/or varpattern(s)

#not todo - always on client side: trimming dates, variable transformations 
```

- indicator homepage with social plugins
