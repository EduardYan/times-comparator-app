"""
This module have some functions
to use in the configuration.
"""

from json import load


def get_config_object() -> dict:
  """
  Return a object with the configuration
  of file './config.json'
  """

  CONFIG_FILE_PATH = './config.json'

  # loading the file of configuration
  object = load(open(CONFIG_FILE_PATH))

  return object


# config object to use
CONFIG = get_config_object()