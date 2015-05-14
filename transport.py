import requests

class NavitiaImplementation:

    def __init__(self, auth_key):
        self.auth_key = auth_key
        self.endpoint = 'https://api.navitia.io/v1/{url}'

    def call(self, url, params=None):
        headers = {'Authorization': self.auth_key}
        return requests.get(self.endpoint.format(url=url), params=params,
                headers=headers).json()

class LocationManager:

    def __init__(self, api_impl):
        self.api = api_impl

    def whereiam(self, latitude, longitude):
        endpoint = 'coord/{latitude};{longitude}'.format(latitude=latitude,
                longitude=longitude)

        return self.api.call(endpoint)

    def get_place(self, place, zone='fr-idf'):
        endpoint = 'coverage/{zone}/places'.format(zone=zone)

        return self.api.call(endpoint, params={'q': place})

    def get_place_id(self, place, zone='fr-idf'):
        if not self.is_place(place):
            return place

        place = self.get_place(place, zone=zone)
        return place['places'][0]['id']

    def is_place(self, location):
        return ';' not in location

    def compute_journey(self, from_place, to_place, zone='fr-idf'):
        endpoint = 'journeys'
        fplace_id = self.get_place_id(from_place, zone)
        tplace_id = self.get_place_id(to_place, zone)

        params = {'from': fplace_id,
                'to': tplace_id}

        return self.api.call(endpoint, params=params)

def initialize_api(auth_key):
    if auth_key == 'INSERT_YOUR_API_KEY_HERE':
        raise RuntimeError("Hey! You didn't set API key !") # based on Shirokamii intelligence (a)

    return LocationManager(NavitiaImplementation(auth_key))
