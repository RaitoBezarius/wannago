# coding: utf8

import math

def convert_duration_to_minutes(seconds):
    return int(math.ceil(seconds / 60.0))

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

        if 'display_informations' in section:
            network = section['display_informations']['network']
            label = section['display_informations']['label']
            self.network_label = str()
            if network == 'Metro':
                self.network_label = 'M{line}'.format(line=label)
            elif network == 'Transilien':
                self.network_label = 'Train {line}'.format(line=label)
            elif network == 'RATP':
                self.network_label = '{line}'.format(line=label)
            else:
                self.network_label = '{net} {line}'.format(net=network, line=label)

    def __str__(self):
        return '{duration} - {type}'.format(duration=self.duration, type=self.type)

class Journey:

    def __init__(self, journey):
        self.duration = convert_duration_to_minutes(journey['duration'])
        self.sections = [Section(section) for section in journey['sections']]
