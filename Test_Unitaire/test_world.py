import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from world import obtenir_continents

class TestObtenirContinents(unittest.TestCase):

    def test_obtenir_continents(self):
        resultats = obtenir_continents()
        
        
        self.assertTrue(any(country == "France" and continent == "Europe" for country, continent in resultats))
        self.assertTrue(any(country == "Brazil" and continent == "South America" for country, continent in resultats))
        self.assertTrue(any(country == "Australia" and continent == "Australia" for country, continent in resultats))
        self.assertTrue(any(country == "United States" and continent == "North America" for country, continent in resultats))
        
        
        self.assertFalse(any(country == "Some Unknown Country" and continent == "Unknown" for country, continent in resultats))

if __name__ == '__main__':
    unittest.main()
