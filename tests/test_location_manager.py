# coding: utf8

from src.transport import initialize_api
import unittest
from unittest.case import SkipTest
import os

@unittest.skipIf(os.getenv('TEST_NAVITIA_API_KEY') is None, reason="No Navitia API key setup for integration tests.")
class TestLocationManager(unittest.TestCase):
    
    def setUp(self):
        self.manager = initialize_api(os.getenv('TEST_NAVITIA_API_KEY').strip())

    def test_whereiam(self):
       result = self.manager.whereiam('2.606791', '48.954081')
       self.assertIn('Avenue de la Libération', result['address']['name'], msg='The API returns an incorrect location.')

    def test_get_place(self):
        result = self.manager.get_place('Villeparisis')
        self.assertIn('Villeparisis', result['places'][0]['name'], msg='The API returns an incorrect location.')

    def test_get_place_id(self):
        result = self.manager.get_place('Villeparisis')
        place_id = result['places'][0]['id']

        self.assertEqual(self.manager.get_place_id('Villeparisis'), place_id)

    def test_is_place(self):
        self.assertTrue(self.manager.is_place('Villeparisis'))
        self.assertFalse(self.manager.is_place('2.5214423;42.141424'))

    def test_compute_journey(self):
        result = self.manager.compute_journey('Villeparisis Mitry le Neuf', 'Grands Boulevards')
