"""This is the main entrypoint for all apps. In this module we
initialize global instances of various packages.
"""
import os
from flask import Flask

# Create new Flask app that will be used as main entrypoint
app = Flask(__name__)
app.config.from_object('config.ProductionConfig')

# Register app blueprints
from apps.views.main import main
from apps.views.time_series import ts as time_series

app.register_blueprint(main, url_prefix='')
app.register_blueprint(time_series, url_prefix='')
