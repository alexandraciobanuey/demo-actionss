import unittest
from dividir import dividir

class TestDividir(unittest.TestCase):

    def test_dividir(self):
        self.assertEqual(dividir(6,2),3)
        self.assertEqual(dividir(18,6),3)
        self.assertEqual(dividir(8,4),2)

if __name__ == '__main__':
    unittest.main()
