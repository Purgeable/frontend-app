from flask import Blueprint, jsonify, render_template
from apps.helpers.custom_api import InnerPath

# Define the blueprint for this application
ts = Blueprint('time_series', __name__)

BASE_URL = '/<string:domain>/series/<string:varname>'

@ts.route(BASE_URL)
def indicator_homepage(domain, varname):
    """Returns html view with latest values, chart and download instructions."""
    ctx = {
        'domain': domain,
        'varname': varname
    }
    return render_template('indicator.html', **ctx)

@ts.route(f'{BASE_URL}/<string:freq>')
@ts.route(f'{BASE_URL}/<string:freq>/<path:inner_path>')
def time_series_api_interface(domain, varname, freq, inner_path=None):
    """Decompose incoming URL into API request."""

    #FIXME: need exception invoker for this
    if freq not in 'dwmqa':
        return jsonify({
            'error': "Frequency value is invalid"
        }), 400
    # ---------------
    ctx = {
        'domain': domain,
        'varname': varname,
        'frequency': freq,
        'rate': None,
        'agg': None,
        'start': None,
        'end': None
    }
    if inner_path is not None:
        optional_args = InnerPath(inner_path).get_dict()
        ctx.update(**optional_args)
    return jsonify(ctx)
