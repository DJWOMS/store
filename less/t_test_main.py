import unittest
from .main import func


class TestFunc(unittest.TestCase):
    """Tests"""
    def test_func_int(self):
        c = func(5, 10)
        self.assertEqual(c, 15)

    def test_func_str(self):
        c = func('5', '8')
        self.assertEqual(c, 13)

    def test_func_error(self):
        with self.assertRaises(ValueError):
            func('5', 'a')


if __name__ == '__main__':
    unittest.main()
