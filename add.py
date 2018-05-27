"""Implement JSON addition.

This should add keys of multiple json objects, add values if the keys are same,
and add recursively, probably controlled by a flag, defaulting to True."""
import json
import logging


class TypeIncompatibilityError(TypeError):
  """Raised when types of objects are not compatible."""
  message = 'Not all objects are compatible with each other.'
  def __init__(self, msg='', value=None, *args):
    msg = msg or self.message
    if value:
      args = args + (value,)
    return super(TypeIncompatibilityError, self).__init__(msg, *args)


# Add some function here to determine diff type compatibility here. Should be
# compatible with all().


def _are_all_compatible(*objects):
  """Tell if all objects are compatible for math operations."""
  # Start with simple soution, the types being same.
  base_type = None
  for obj in objects:
    obj_type = type(obj)
    if not base_type:
      base_type = obj_type
    elif base_type != obj_type:
      return False
  return True
  # # Another approach.
  # first = objects[0]
  # start = type(first)()  # base_additive
  # try:
  #   _ = sum(objects, start)
  # except TypeError as e:
  #   _, value, traceback = sys.exc_info()
  #   # Value can be sent as 2nd expression, with 1st just a class, not an obj.
  #   logging.error(str(e))
  #   # Do not raise, just log it.
  #   raise TypeIncompatibilityError(value=value), None, traceback


def add(*args):
  """Add json/dict objects."""
  # Provide way of passing options to json.loads via kwargs.
  objects = map(json.loads, args)
  if not _are_all_compatible(objects):
    raise TypeIncompatibilityError()
  return json.dumps(_add(*objects))

def _add(*args):
  if all(hasattr(obj, '__add__') for obj in args):
    start = type(args[0])()  # base_additive
    return sum(args, start)
  elif isinstance(args[0], dict):
    result = {}
    for key, value in sum((d.items() for d in args), []):
      if key not in result:
        result[key] = value
      else:
        result[key] = _add(result[key], value)
    return result
  raise TypeIncompatibilityError()



