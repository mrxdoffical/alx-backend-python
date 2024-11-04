import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Test case for the access_nested_map function.
    """

    @parameterized.expand([
        ({}, ["a"]),
        ({"a": 1}, ["a", "b"]),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Test access_nested_map raises KeyError for invalid paths.

        Parameters:
        nested_map (dict): The nested map to be accessed.
        path (list): The sequence of keys to access the value.
        """
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)

        exception = cm.exception
        self.assertEqual(exception.args[0], path[-1])


if __name__ == '__main__':
    unittest.main()
