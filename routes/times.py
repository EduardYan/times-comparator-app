"""
This module have the routes to use
in the server.
"""


from flask import Blueprint, redirect, render_template, request, url_for, flash
from helpers.utils import save_time_in_file, get_time_current, comparate_time, InvalidTime

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

    try:
      # saving in a file
      save_time_in_file(float(new_time))

      flash('Time Setted Succesfully')

      return redirect(url_for('times.index'))

    except ValueError:
      # in case the new time not is valid for pass to float value
      flash('The time for set not is valid.')

      return redirect(url_for('times.index'))


@times_routes.route('/comparate-time', methods = ['POST'])
def comparate_time_route():
  """
  Route for comparate the time
  with the time setted.
  """

  # getting the time to comparate
  time_to_comparate = request.form['time-to-comparate']

  try:
    # getting the difference
    difference_value = comparate_time(time_to_comparate)

    return render_template('result-comparation.html', difference_value = difference_value)

  except ValueError:
      # in case the new time not is valid for pass to float value
      # into the function
      flash('The time to comparate not is valid.')

      return redirect(url_for('times.index'))


@times_routes.route('/about')
def about():
  """
  Route for render the about page.
  """

  return render_template('about.html')