"""Decompose custom URL.

    URL format (? marks optional parameter):

    {domain}/series/{varname}/{freq}/{?suffix}/{?start}/{?end}/{?finaliser}

    Examples:
        oil/series/BRENT/m/eop/2015/2017/csv
        ru/series/EXPORT_GOODS/m/bln_rub

    Tokens:
        {domain} is reserved, future use: 'all', 'ru', 'oil', 'ru:bank', 'ru:77'

        {varname} is GDP, GOODS_EXPORT, BRENT (capital letters with underscores)

        {freq} is any of:
            a (annual)
            q (quarterly)
            m (monthly)
            w (weekly)
            d (daily)

        {?suffix} may be:

            unit of measurement (unit):
                example: bln_rub, bln_usd, tkm

            rate of change for real variable (rate):
                rog - change to previous period
                yoy - change to year ago
                base - base index

            aggregation command (agg):
                eop - end of period
                avg - average

    To integrate here:
        <https://github.com/mini-kep/frontend-app/blob/master/apps/views/time_series.py>

Decomposition procedure involves:

    CustomGET class
    InnerPath class
    to_csv()

"""

from datetime import date

import pandas as pd
import requests


ALLOWED_FREQUENCIES = ('d', 'w', 'm', 'q', 'a')

ALLOWED_REAL_RATES = (
    'rog',
    'yoy',
    'base'
)
ALLOWED_AGGREGATORS = (
    'eop',
    'avg'
)
ALLOWED_FINALISERS = (
    'info',  # resereved: retrun json with variable and url description
    'csv',   # to implement: return csv (default)
    'json',  # to implement: return list of dictionaries
    'xlsx'   # resereved: return Excel file
)

# http, not https
ENDPOINT = 'http://minikep-db.herokuapp.com/api/datapoints'


def make_freq(freq: str):
    if freq not in ALLOWED_FREQUENCIES:
        raise InvalidUsage(f'Frequency <{freq}> is not valid')
    return freq


class InvalidUsage(Exception):
    """Shorter version of
       <http://flask.pocoo.org/docs/0.12/patterns/apierrors/>.

       Must also register a handler (see link above).
    """
    status_code = 400

    def __init__(self, message, status_code=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code

    def to_dict(self):
        return dict(message=self.message)


class TokenHelper:
    def __init__(self, tokens: list):
        self.tokens = tokens

    def get_dates_dict(self):
        start_year, end_year = self._find_years()
        result = {}
        if start_year:
            result['start_date'] = self._as_date(start_year, month=1, day=1)
        if end_year:
            result['end_date'] = self._as_date(end_year, month=12, day=31)
        return result

    def fin(self):
        return self._find_one(ALLOWED_FINALISERS)

    def rate(self):
        return self._find_one(ALLOWED_REAL_RATES)

    def agg(self):
        return self._find_one(ALLOWED_AGGREGATORS)

    def _find_years(self):
        """Extract years from *tokens* list. Pops values found away from *tokens*."""
        start, end = None, None
        integers = [x for x in self.tokens if x.isdigit()]
        if len(integers) in (1, 2):
            start = integers[0]
            self._pop(start)
        if len(integers) == 2:
            end = integers[1]
            self._pop(end)
        return start, end

    @staticmethod
    def _as_date(year: str, month: int, day: int):
        """Generate YYYY-MM-DD dates based on components."""
        return date(year=int(year),
                    month=month,
                    day=day).strftime('%Y-%m-%d')

    def _pop(self, value):
        self.tokens.pop(self.tokens.index(value))

    def _find_one(self, allowed_values):
        """Find entries of *allowed_values* into *tokens*.
           Pops values found away from *tokens*.
        """
        values_found = [p for p in allowed_values if p in self.tokens]
        if not values_found:
            return None
        elif len(values_found) == 1:
            x = values_found[0]
            self._pop(x)
            return x
        else:
            raise InvalidUsage(values_found)


class InnerPath:

    def __init__(self, inner_path: str):
        """Extract parameters from *inner_path* string.

           Args:
              inner_path is a string like 'eop/2015/2017/csv'

           Methods:
              get_dict() returns inner path tokens as dictionary
        """
        # list of non-empty strings
        tokens = [token.strip() for token in inner_path.split('/') if token]
        helper = TokenHelper(tokens)
        # extract dates
        self.dict = helper.get_dates_dict()
        # finaliser and transforms
        self.dict['fin'] = helper.fin()
        self.dict['rate'] = helper.rate()
        self.dict['agg'] = helper.agg()
        if self.dict['rate'] and self.dict['agg']:
            raise InvalidUsage("Cannot combine rate and aggregation.")
        # find unit name, if present
        if tokens:
            self.dict['unit'] = tokens[0]
        else:
            self.dict['unit'] = self.dict['rate'] or None

    def get_dict(self):
        return self.dict


class CustomGET:

    @staticmethod
    def make_name(varname, unit=None):
        name = varname
        if unit:
            name = f'{name}_{unit}'
        return name

    def __init__(self, domain, varname, freq, inner_path):
        ip = InnerPath(inner_path).get_dict()
        self.params = dict(name=self.make_name(varname, ip['unit']),
                           freq=make_freq(freq))
        for key in ['start_date', 'end_date']:
            val = ip.get(key)
            if val:
                self.params[key] = val

    def get_csv(self):
        return call_db_api(self.params, fmt='csv')


def call_db_api(params, fmt, endpoint=ENDPOINT):
    params['format'] = fmt
    r = requests.get(endpoint, params=params)
    if r.status_code == 200:
        return r.text
    else:
        msg = f'Cannot read {params} from {endpoint}.'
        raise InvalidUsage(msg)

