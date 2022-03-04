"""
This file have the web app
configurations and creating initials.
For execute the server is the file 'index.py'

"""

from flask import Flask
from routes.times import times_routes


# creating the server
app = Flask(__name__)


# setting the routes
app.register_blueprint(times_routes)