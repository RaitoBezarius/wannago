# coding: utf8

from src.transport import NavitiaImplementation
import unittest
from unittest import mock


class TestNavitiaImplementation(unittest.TestCase):

    def test_endpoint(self):
        impl = NavitiaImplementation('anything')
        self.assertEqual(impl.endpoint, 'https://api.navitia.io/v1/{url}')

    def test_auth_key(self):
        impl = NavitiaImplementation('anything')
        self.assertEqual(impl.auth_key, 'anything')

    @mock.patch('src.transport.requests')
    def test_call(self, reqMock):
        impl = NavitiaImplementation('anything')

        resultMock = mock.MagicMock()
        resultMock.json.return_value = '{}'
        reqMock.get.return_value = resultMock

        self.assertEqual(impl.call('test'), '{}')

        reqMock.get.assert_called_with(impl.endpoint.format(url='test'),
                                       params=None,
                                       headers={'Authorization': impl.auth_key})
