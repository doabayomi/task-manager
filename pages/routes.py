from flask import url_for, render_template, redirect
import requests
from . import pages_blueprint
from flask_security import auth_required


@pages_blueprint.route('/')
def root():
    return redirect(url_for('auth.login'))


@pages_blueprint.route('/dashboard')
@auth_required()
def dashboard():
    try:
        api_url = url_for('taskresource', _external=True)
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error for HTTP errors
        tasks = response.json()  # Parse JSON response
    except requests.RequestException as e:
        print(f"Error fetching tasks: {e}")
        tasks = []  # Fallback to an empty l
    return render_template('dashboard.html', tasks=tasks)


@pages_blueprint.route('/edit_profile')
@auth_required()
def edit_profile():
    return render_template('profile.html')
