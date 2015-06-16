# coding: utf8

import requests
import arrow
from config import defaultConfig


class NavitiaImplementation:

    def __init__(self, auth_key):
        self.auth_key = auth_key
        self.endpoint = 'https://api.navitia.io/v1/{url}'

    def call(self, url, params=None):
        headers = {'Authorization': self.auth_key}
        result = requests.get(self.endpoint.format(url=url),
                              params=params,
                              headers=headers).json()
        if 'error' in result:
            raise RuntimeError('Error when querying Navitia API: {msg}. ({prms})'
                    .format(msg=result['error']['message'],
                    prms=params))
        return result


class LocationManager:

    def __init__(self, api_impl):
        self.api = api_impl
        self.aliases = defaultConfig.getSection('Aliases')
        self.default_zone = defaultConfig.getConfig('Coverage',
                                                    'DefaultZone',
                                                    defaultValue='fr-idf',
                                                    writeIfMissing=True)

    def whereiam(self, latitude, longitude):
        endpoint = 'coord/{latitude};{longitude}'.format(latitude=latitude,
                                                         longitude=longitude)

        return self.api.call(endpoint)

    def get_place(self, place):
        endpoint = 'coverage/{zone}/places'.format(zone=self.default_zone)

        return self.api.call(endpoint, params={'q': place})

    def get_place_id(self, place):
        if not self.is_place(place):
            return place

        if place in self.aliases:
            return self.aliases[place]

        place = self.get_place(place)
        return place['places'][0]['id']

    def is_place(self, location):
        return ';' not in location

    def compute_journey(self, from_place, to_place):
        endpoint = 'journeys'
        fplace_id = self.get_place_id(from_place)
        tplace_id = self.get_place_id(to_place)

        params = {'from': fplace_id,
                  'to': tplace_id,
                  'datetime': arrow.now().format('YYYYMMDDHHmmss')}

        return self.api.call(endpoint, params=params)


def initialize_api(auth_key):
    if auth_key is not None:
        defaultConfig.setToken(auth_key)
    else:
        auth_key = defaultConfig.getToken()
        if auth_key is None:
            print('Please set your API token using \'-t\' option and try again')
            exit(1)
    return LocationManager(NavitiaImplementation(auth_key))
