# coding: utf8

from src.config import Config
import unittest
from unittest import mock


class TestLocationManager(unittest.TestCase):

    @mock.patch('src.transport.defaultConfig')
    def test_default_zone(self, defaultConfigMock):
        from src.transport import LocationManager
        defaultConfigMock.getConfig.return_value = 'fr-idf'
        manager = LocationManager(None)
        self.assertEqual(manager.api, None)
        self.assertEqual(manager.default_zone, 'fr-idf')
        defaultConfigMock.getConfig.assert_called_with('Coverage',
                                                       'DefaultZone',
                                                       defaultValue='fr-idf',
                                                       writeIfMissing=True)


class TestConfigStore(unittest.TestCase):

    def test_set_config(self):
        pass

    def test_get_config(self):
        pass

    def test_get_section(self):
        pass

    def test_set_token(self):
        pass

    def test_get_token(self):
        pass

    def test_write_config(self):
        pass

    def test_initialize_config(self):
        pass
