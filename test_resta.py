import unittest
from resta import resta

class TestResta(unittest.TestCase):

    def test_resta(self):
        self.assertEqual(resta(7,2),5)
        self.assertEqual(resta(1,1),0)
        self.assertEqual(resta(-3,-1),-2)

if __name__ == '__main__':
    unittest.main()
