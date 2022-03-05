"""
Some utils functions to use.
"""

from models.time_number import TimeNumber

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
    raise InvalidTime('The time passed must be a float value.')

  else:
    with open(FILE_TO_SAVE_TIME, 'w') as f:
      f.write(
        str(time)
      )


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

    time_number = TimeNumber(content)

    return time_number

  except:
    # in case some problem to read the file
    print('Problems to read the file.')


def comparate_time(to_comparate:float) -> float:
  """
  Comparate the time passed
  for parameter with the setted
  in the file of the time.

  ValueError execption if the parameter
  to_comparate value it can't convert
  to float number.

  """

  # getting the direfference between the time current and the time to comparate
  time_current = get_time_current()

  difference = float(time_current.value - float(to_comparate))

  return difference