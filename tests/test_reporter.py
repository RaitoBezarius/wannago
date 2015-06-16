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

        api = FakeAPI(""" {
            "journeys": [
                {
                    "duration": 600,
                    "departure_date_time": "20150902T144228",
                    "arrival_date_time": "20150902T174230",
                    "sections": [
                        {
                           "duration": 600,
                           "type": "public_transport",
                           "from": {
                                "id": "123",
                                "embedded_type": "stop_area",
                                "name": "Paris"
                            },
                            "to": {
                                "id": "123",
                                "embedded_type": "stop_area",
                                "name": "New York"
                            },
                            "display_informations": {
                                "network": "RATP",
                                "physical_mode": "Métro",
                                "label": "7",
                                "color": "E2B3D1"
                            }
                        },
                        {
                           "duration": 1500,
                           "type": "public_transport",
                           "from": {
                                "id": "123",
                                "embedded_type": "stop_area",
                                "name": "Paris"
                            },
                            "to": {
                                "id": "123",
                                "embedded_type": "stop_area",
                                "name": "New York"
                            },
                            "display_informations": {
                                "network": "Transilien",
                                "physical_mode": "K",
                                "label": "K",
                                "color": "E2B3D1"
                            }
                        },
                        {
                           "duration": 600,
                           "type": "public_transport",
                           "from": {
                                "id": "123",
                                "embedded_type": "stop_area",
                                "name": "Paris"
                            },
                            "to": {
                                "id": "123",
                                "embedded_type": "stop_area",
                                "name": "New York"
                            },
                            "display_informations": {
                                "network": "RATP",
                                "physical_mode": "Tramway",
                                "label": "3a",
                                "color": "E2B3D1"
                            }
                        },
                        {
                           "duration": 600,
                           "type": "public_transport",
                           "from": {
                                "id": "123",
                                "embedded_type": "stop_area",
                                "name": "Paris"
                            },
                            "to": {
                                "id": "123",
                                "embedded_type": "stop_area",
                                "name": "New York"
                            },
                            "display_informations": {
                                "network": "YouveNeverHeardAboutIt",
                                "physical_mode": "o_o",
                                "label": "w_w",
                                "color": "E2B3D1"
                            }
                        },
                        {
                            "duration": 900,
                            "type": "street_network",
                            "from": {
                                "id": "345",
                                "embedded_type": "stop_area",
                                "name": "New York"
                            },
                            "to": {
                                "id": "567",
                                "embedded_type": "address",
                                "name": "Random New York Address"
                            },
                            "path": [
                                {
                                    "length": 300
                                },
                                {
                                    "length": 250
                                },
                                {
                                    "length": 900
                                }
                            ],
                            "length": 1450
                        }
                    ]
                }
            ]
        } """)

        message = report_journey(api, 'somewhere', 'someto')
        self.assertIn('10 mn', message)
        self.assertIn('M7', message)
        self.assertIn('New York', message)
        self.assertIn('Walk', message)
        self.assertIn('1450 meter', message)
        self.assertIn('Train', message)
