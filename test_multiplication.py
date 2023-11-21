import unittest
from multiplication import multiplication

class TestMultiplication(unittest.TestCase):

    def test_multiplication(self):
        self.assertEqual(multiplication(3,2),6)
        self.assertEqual(multiplication(6,3),18)
        self.assertEqual(multiplication(1,5),5)

if __name__ == '__main__':
    unittest.main()
