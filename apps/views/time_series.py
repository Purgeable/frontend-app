from flask import Blueprint, jsonify
from apps.helpers.url_decomposer import decompose_inner_path

# Define the blueprint for this application
ts = Blueprint('time_series', __name__)

@ts.route('/<string:domain>/<series>/<string:varname>/<string:freq>')
@ts.route('/<string:domain>/<series>/<string:varname>/<string:freq>/<path:inner_path>')
def landing_page(domain, series, varname, freq, inner_path=None):
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
        opt_args = decompose_inner_path(inner_path)
        ctx.update(**opt_args)
    return jsonify(ctx)
