import unittest
from unnecessary_math1 import again
class TestUM(unittest.TestCase):
 
    def setUp(self):
        pass
    def test_random_youwant(self):
        self.assertEqual(again('a',3), 'aaa')
 
if __name__ == '__main__':
    unittest.main()













