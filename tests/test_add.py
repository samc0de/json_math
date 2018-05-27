import json
import unittest

from context import add


class AddTest(unittest.TestCase):
  """Tests add function of add.py."""
  def test_asserts_type_equality(self):
    """Tests whether add() checks type compatibility."""
    raise ValueError()
    a_list = json.dumps(range(4))
    a_dict = json.dumps(dict(enumerate('abcd')))
    self.assertRaises(add.TypeIncompatibilityError, add.add, a_list, a_dict)

  def test_add(self):
    """Test basic addition."""
    json_1 = json.dumps({
        'foo': 1,
        'bar': 'a'
        })
    json_2 = json.dumps({
        'baz': 'baz'
        })
    actual = add.add(json_1, json_2)
    expected = json.dumps({
        'foo': 1,
        'bar': 'a',
        'baz': 'baz'
        })
    self.assertEqual(expected, actual)


class AreAllCompatibleTest(unittest.TestCase):
  def test_all_same_type_list(self):
    """Test behaviour when all objects are of same type."""
    objects = map(json.dumps, (['abc', 2, 'a'], range(4), ['foo', 'bar']))
    self.assertTrue(add._are_all_compatible(objects))


if __name__ == '__main__':
  unittest.main()
