from flask import Blueprint, render_template_string
from .df_values import dfa, dfm, dfq

# Define the blueprint for this application
main = Blueprint('main', __name__)

@main.route('/annual/')
def annual():
    content = dfa.to_csv()
    return render_template_string(content)

@main.route('/quarterly/')
def quarterly():
    content = dfq.to_csv()
    return render_template_string(content)

@main.route('/monthly/')
def monthly():
    content = dfm.to_csv()
    return render_template_string(content)
