import sys
import unittest
from unittest import mock
import json

class TestLocationManager(unittest.TestCase):
    
    @mock.patch('src.transport.defaultConfig')
    def test_default_zone(self, defaultConfigMock):
        from src.transport import LocationManager
        defaultConfigMock.getConfig.return_value = 'fr-idf'
        manager = LocationManager(None)
        self.assertEqual(manager.api, None)
        self.assertEqual(manager.default_zone, 'fr-idf')
        defaultConfigMock.getConfig.assert_called_with('Coverage', 'DefaultZone',
                defaultValue='fr-idf', writeIfMissing=True)
            
