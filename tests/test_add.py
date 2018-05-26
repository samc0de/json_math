import unittest


class AddTest(unittest.TestCase):
  """Tests add function of add.py."""
  def test_add(self):
    """Test basic addition."""
    json_1 = {
        'foo': 1,
        'bar': 'a'
        }
    json_2 = {
        'baz': 'baz'
        }
    actual = add.add(json_1, json_2)
    expected = {
        'foo': 1,
        'bar': 'a',
        'baz': 'baz'
        }
    self.assertEqual(expected, actual)


if __name__ == '__main__':
  unittest.main()
