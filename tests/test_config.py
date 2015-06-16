# coding: utf8

from src.config import Config
import unittest
from unittest import mock
import configparser


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

class ConfigTestWrapper(Config):

    def __init__(self, cfg_file):
        self.cfg = configparser.ConfigParser()
        self.config_file = cfg_file

    def writeConfig(self):
        m = mock.mock_open()
        with mock.patch('src.config.open'.format(__name__), m, create=True):
            super(ConfigTestWrapper, self).writeConfig()
        return m



class TestConfigStore(unittest.TestCase):
    
    def setUp(self):
        self.config_file = "wannago.conf"
        self.defaultConfig = ConfigTestWrapper(self.config_file)

    def test_set_config(self):
        self.defaultConfig.setConfig('Test1', 'NewValue', '1')
        self.assertEqual(self.defaultConfig.getConfig('Test1', 'NewValue'), '1')
        self.defaultConfig.setConfig('Test1', 'New_Value', '2')
        self.assertEqual(self.defaultConfig.getConfig('Test1', 'New_Value'), '2')
        self.defaultConfig.setConfig('Test1', 'New_Value', '3')
        self.assertEqual(self.defaultConfig.getConfig('Test1', 'New_Value'), '3')
        self.defaultConfig.setConfig('Test1', 'New_Value', '3', overwrite=False)
        self.assertEqual(self.defaultConfig.getConfig('Test1', 'New_Value'), '3')
    
    def test_get_config(self):
        self.defaultConfig.setConfig('Test1', 'NewValue', '15')
        self.assertEqual(self.defaultConfig.getConfig('Test1', 'NewValue'), '15')
        self.assertEqual(self.defaultConfig.getConfig('Test1', 'NewValue', '20'), '15')
        self.assertEqual(self.defaultConfig.getConfig('Test2', 'Aha', defaultValue='1'), '1')

    def test_get_section(self):
        self.assertEqual(self.defaultConfig.getSection('NULL', defaultValue=['a', 'b']), ['a', 'b'])
        self.assertEqual(self.defaultConfig.getSection('NULL'), [])

    def test_write_config(self):
        m_open = self.defaultConfig.writeConfig()
        m_open.assert_called_once_with(self.config_file, 'w')
