# coding: utf8

from src.reporter import report_journey
import unittest
import json


class TestReportingSystem(unittest.TestCase):

    def test_report_journey(self):
        class FakeAPI:

            def __init__(self, fake_data):
                self.fake_data = fake_data

            def compute_journey(self, from_place, to_place):
                return json.loads(self.fake_data)

        api = FakeAPI(''' {
            'journeys': [
                {
                    'duration': 600,
                    'departure_date_time': '20150902T144228',
                    'arrival_date_time': '20150902T174230',
                    'sections': [
                        {
                           'duration': 600,
                           'type': 'public_transport',
                           'from': {
                                'id': '123',
                                'embedded_type': 'stop_area',
                                'name': 'Paris'
                            },
                            'to': {
                                'id': 123,
                                'embedded_type': 'stop_area',
                                'name': 'New York'
                            },
                            'display_informations': {
                                'network': 'RyanTransport',
                                'physical_mode': 'Teleportation',
                                'label': 'Alpha',
                                'color': 'E2B3D1'
                            }
                        }
                    ]
                }
            ]
        } ''')

        message = report_journey(api, 'somewhere', 'someto')
        self.assertIn('10 mn', message)
        self.assertIn('RyanTransport', message)
        self.assertIn('New York', message)
