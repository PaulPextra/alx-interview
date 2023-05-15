#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
  """
  Method that determines if a given data set
  represents a valid UTF-8 encoding
  """
  
  num_of_bytes = 0
  for byte in data:
    # Check if the current byte is a continuation byte
    if num_of_bytes == 0:
      if byte >> 5 == 0b110:
        num_of_bytes = 1
      elif byte >> 4 == 0b1110:
        num_of_bytes = 2
      elif byte >> 3 == 0b11110:
        num_bytes = 3
      elif byte >> 7 == 1:
        return False
    else:
      # Check if the current byte is a continuation byte
      if byte >> 6 != 0b10:
        return False
      num_of_bytes -= 1

  return num_of_bytes == 0
