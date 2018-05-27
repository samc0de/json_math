import json
import unittest

from context import add


# class AddTest(unittest.TestCase):
#   """Tests add function of add.py."""
#   def test_asserts_type_equality(self):
#     """Tests whether add() checks type compatibility."""
#     a_list = range(4)
#     a_dict = dict(enumerate('abcd'))
#     self.assertRaises(add.TypeIncompatibilityError, add.add, a_list, a_dict)
# 
#   def test_add(self):
#     """Test basic addition."""
#     json_1 = {
#         'foo': 1,
#         'bar': 'a'
#         }
#     json_2 = {
#         'baz': 'baz'
#         }
#     actual = add.add(json_1, json_2)
#     expected = {
#         'foo': 1,
#         'bar': 'a',
#         'baz': 'baz'
#         }
#     self.assertEqual(expected, actual)


class AreAllCompatibleTest(unittest.TestCase):
  def test_all_same_type_list(self):
    """Test behaviour when all objects are of same type."""
    objects = map(json.dumps, (['abc', 2, 'a'], range(4), ['foo', 'bar']))
    self.assertTrue(add._are_all_compatible(objects))


if __name__ == '__main__':
  unittest.main()
