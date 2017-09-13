[![Build Status](https://travis-ci.org/mini-kep/frontend-app.svg?branch=master)](https://travis-ci.org/mini-kep/frontend-app) 
[![Coverage badge](https://codecov.io/gh/mini-kep/frontend-app/branch/master/graphs/badge.svg)](https://codecov.io/gh/mini-kep/frontend-app)

# mini-kep-app
Flask app with API to get macroeconomic time series

## v.0.1 - relay three CSVs by github webhook + intro at frontpage

#### App address:

   - <http://mini-kep.herokuapp.com>

#### Frontpage:

  - code example with highlighting  
  
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

The logic of [the test](https://github.com/mini-kep/frontend-app/blob/master/apps/tests/test_integrity.py)
is assure identity of the csv files at parent repo ant and app data interfaces.


## Testing approach:

Important comments are [here](https://github.com/mini-kep/frontend-app/issues/7)

## Proposed enhancements:

- see listing at [issue 1](https://github.com/epogrebnyak/mini-kep-app/issues/1)

