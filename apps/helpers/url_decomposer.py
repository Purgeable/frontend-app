"""Decompose time series API URL."""
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
    'info',
    'csv',
    'json', # which should be default
    'xlsx'
)

def _get_years(tokens):
    start, end = None, None
    integers = [x for x in tokens if x.isdigit()]
    if len(integers) == 1:
        start = integers[0]
    elif len(integers) == 2:
        start = integers[0]
        end = integers[1]
    return start, end

def _assign_values(tokens, allowed_values):
    postfix = [p for p in allowed_values if p in tokens]
    if not postfix:
        return None
    elif len(postfix) == 1:
        return postfix[0]
    else:
        raise ValueError(tokens)

def decompose_inner_path(inner_tokens):
    inner_tokens = [x.strip() for x in inner_tokens.split('/') if x]
    start, end = _get_years(inner_tokens)
    return dict(rate=_assign_values(inner_tokens, ALLOWED_REAL_RATES),
                agg=_assign_values(inner_tokens, ALLOWED_AGGREGATORS),
                start=start,
                end=end)
