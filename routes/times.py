"""
This module have the routes to use
in the server.
"""


import time
from flask import Blueprint, redirect, render_template, request, url_for
from helpers.utils import save_time_in_file, get_time_current

# routes
times_routes = Blueprint('times', __name__)


@times_routes.route('/')
def index():
  """
  Principal route for the server.
  """

  # getting the time current to pass of the view
  time_current = get_time_current()


  return render_template('index.html', time_current = time_current)


@times_routes.route('/set-time', methods = ['POST'])
def set_time():
  """
  Route for set a time to comparate.
  Only run for POST method
  """

  if request.method == 'POST':

    # getting the values to set
    new_time = request.form['new-time']

    # saving in a file
    save_time_in_file(new_time)

    return redirect(url_for('times.home'))


@times_routes.route('/about')
def about():
  """
  Route for render the about page.
  """

  return render_template('about.html')