from flask import Blueprint, jsonify, render_template
import apps.helpers.custom_api as custom_api

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


@ts.errorhandler(custom_api.InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@ts.route(f'{BASE_URL}/<string:freq>')
@ts.route(f'{BASE_URL}/<string:freq>/<path:inner_path>')
def time_series_api_interface(domain, varname, freq, inner_path=None):
    return custom_api.CustomGET(domain, varname, freq, inner_path).get_csv()