from flask import url_for, render_template, redirect
from . import pages_blueprint
from flask_security import auth_required


@pages_blueprint.route('/')
def root():
    return redirect(url_for('auth.login'))


@pages_blueprint.route('/dashboard')
@auth_required()
def dashboard():
    return render_template('dashboard.html')


@pages_blueprint.route('/edit_profile')
@auth_required()
def edit_profile():
    return render_template('profile.html')
