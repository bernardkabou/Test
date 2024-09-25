import unittest
import os
import sys

# Ajout du chemin vers src dans sys.path pour ouvoir importer le module addistion
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from add import addition

class TestAddition(unittest.TestCase): 
    def test_positif(self):
        self.assertEqual(addition(2, 3,), 5)
        
        def test_negative(self):
            self.assertEqual(addition(-1, 1), 0)
            
            if __name__ == '__main__':
                unittest.main()