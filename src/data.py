# coding: utf8

import math
import arrow

def convert_duration_to_minutes(seconds):
    return int(math.ceil(seconds / 60.0))

def convert_datetime(date):
    return arrow.get(date, 'YYYYMMDDTHHmmss')

class Subsection:

    def __init__(self, subsection):
        self.id = subsection['id']
        self.type = subsection['embedded_type']
        self.name = subsection['name']

class Section:

    def __init__(self, section):
        self.duration = convert_duration_to_minutes(section['duration'])
        self.type = section['type']
        if self.type != 'waiting' and self.type != 'crow_fly':
            self.from_section = Subsection(section['from'])
            self.to_section = Subsection(section['to'])

        if self.type == 'street_network':
            self.length = 0
            for path in section['path']:
                self.length += path['length']

        if 'display_informations' in section:
            network = section['display_informations']['network']
            physical_mode = section['display_informations']['physical_mode']
            label = section['display_informations']['label']
            self.color = section['display_informations']['color']
            self.has_color = bool(self.color)
            self.network_label = str()
            if network == 'Transilien':
                self.network_label = 'Train {line}'.format(line=label)
            elif network == 'RATP':
                if physical_mode == 'Métro':
                    self.network_label = 'M{line}'.format(line=label)
                else:
                    self.network_label = '{line}'.format(line=label)
            else:
                self.network_label = '{net} {line}'.format(net=network,
                                                           line=label)

    def __str__(self):
        return '{duration} - {type}'.format(duration=self.duration,
                                            type=self.type)

class Journey:

    def __init__(self, journey):
        self.duration = convert_duration_to_minutes(journey['duration'])
        self.start_time = convert_datetime(journey['departure_date_time'])
        self.end_time = convert_datetime(journey['arrival_date_time'])
        self.sections = [Section(section) for section in journey['sections']]
