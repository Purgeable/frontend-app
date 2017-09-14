"""Decompose time series API URL."""

allowed_real_rate = ['rog', 'yoy', 'base']
allowed_aggregator = ['eop', 'avg']
allowed_finaliser = ['info', 'csv']


def as_int(s):
    try:
        return int(s)
    except ValueError:
        return None


def get_integers(tokens):
    start, end = None, None
    integers = [x for x in tokens if as_int(x) is not None]
    if len(integers) == 1:
        start = integers[0]
    elif len(integers) == 2:
        start = integers[0]
        end = integers[1]
    return start, end     
    

def assign(tokens, allowed_values):
    postfix = [p for p in allowed_values if p in tokens]
    if len(postfix) == 0:
        return None
    elif len(postfix) == 1:   
        return postfix[0]
    else:
        raise ValueError(tokens)    


def decompose_inner_path(inner_tokens):
    start, end = get_integers(inner_tokens)
    return dict(rate=assign(inner_tokens, allowed_real_rate),
                agg=assign(inner_tokens, allowed_aggregator),
                start=start,
                end=end)
    

def parse_api_url(url):
    tokens = [x.strip() for x in url.split("/") if x]
    assert len(tokens) >= 4
    d1 = dict(domain=tokens[0],
              name=tokens[2],
              freq=tokens[3])
    if len(tokens) >= 4:
        d2 = decompose_inner_path(tokens[4:])
    else:
        d2 = decompose_inner_path(inner_tokens=[])
    d1.update(d2)    
    return d1


calls = """/ru/series/GDP/a/
/ru/series/GDP/q/rog
/ru/series/GDP/q/yoy
/ru/series/GDP/q/base""".split("\n")


assert parse_api_url('/ru/series/GDP/q/base/1998/2017') ==  {'agg': None,
 'domain': 'ru',
 'end': '2017',
 'freq': 'q',
 'name': 'GDP',
 'rate': 'base',
 'start': '1998'}


assert parse_api_url('/oil/series/BRENT/m/avg/1991/') ==  {'agg': 'avg',
 'domain': 'oil',
 'end': None,
 'freq': 'm',
 'name': 'BRENT',
 'rate': None,
 'start': '1991'}    
