from flask import send_from_directory, render_template
from . import pages_blueprint


@pages_blueprint.route('/')
def root():
    return render_template('index.html')


@pages_blueprint.route('/test')
def test():
    return render_template('login.html')
