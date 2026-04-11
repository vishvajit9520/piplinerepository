import unittest
from math_utils import add

class TestMath(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 6)  # ❌ Wrong expected value (bug)

if __name__ == '__main__':
    unittest.main()
