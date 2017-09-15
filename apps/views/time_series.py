from flask import Blueprint, jsonify, render_template
from apps.helpers.url_decomposer import decompose_inner_path

# Define the blueprint for this application
ts = Blueprint('time_series', __name__)

BASE_URL = '/<string:domain>/<series>/<string:varname>'

@ts.route(BASE_URL)
def indicator_homepage(domain, series, varname, freq):
    """Returns html view with latest values, chart and download instructions."""
    ctx = {
        'domain': domain,
        'series': series,
        'varname': varname,
    }
    return render_template('ts_landing.html', **ctx)

@ts.route(f'{BASE_URL}/<string:freq>/<path:inner_path>')
def time_series_api(domain, series, varname, freq, inner_path):
    if freq not in 'dwmqa':
        return jsonify({
            'error': "Frequency value is invalid"
        }), 400
    ctx = {
        'domain': domain,
        'series': series,
        'varname': varname,
        'frequency': freq
    }
    if inner_path is not None:
        optional_args = decompose_inner_path(inner_path)
        ctx.update(**optional_args)
    return jsonify(ctx)
