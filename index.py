"""
Principal file for execute
the server.
"""

from app import app
from helpers.config import CONFIG



if __name__ == '__main__':
  # running the server
  app.run(
    port = CONFIG['PORT'],
    debug = True
  )