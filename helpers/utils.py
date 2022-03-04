"""
Some utils functions to use.
"""


# path for file
FILE_TO_SAVE_TIME = 'data/time.txt'


class InvalidTime(TypeError):
  """
  Error Model in case the time is invalid
  """
  pass


def save_time_in_file(time:float) -> None:
  """
  Save the time passed
  for parameter in a file.
  """

  # validating the datatype
  if type(time) not in [float]:
    InvalidTime('The time passed must be a float value.')



  with open(FILE_TO_SAVE_TIME, 'w') as f:
    f.write(time)


def get_time_current() -> float:
  """
  Return the time current in the file where
  is the time configuration.
  """
  
  # open and reading
  try:
    with open(FILE_TO_SAVE_TIME, 'r') as f:
      content = f.read()

    # converting to floating number
    content = float(content)

    return content

  except:
    print('Problems to read the file.')