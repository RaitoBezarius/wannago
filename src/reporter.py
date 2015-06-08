# coding: utf8

from data import Journey
from color import format_color


def format_datetime(arrow_time):
    return '{h}h{m}'.format(h=arrow_time.format('HH'),
                            m=arrow_time.format('mm'))


def report_journey(api, from_place, to_place, without=None):
    resp = api.compute_journey(from_place, to_place)
    journey = Journey(resp['journeys'][0])

    message = '[{duration} mn] - [{start}]\n{path}\n[{end}]'
    subpaths = []
    for section in journey.sections:
        if section.type == 'public_transport':
            subpath = '==> {net_label} - {to_place} [{duration} mn]'
            subpath = subpath.format(net_label=section.network_label,
                                     to_place=section.to_section.name,
                                     duration=section.duration)

            if section.has_color:
                subpath = format_color(section.color, subpath)

            subpaths.append(subpath)
        elif section.type == 'street_network' and section.length >= 300:
            subpath = '==> Walk to {to_place} [{duration} mn - {length} meter]'
            subpath = subpath.format(to_place=section.to_section.name,
                                     duration=section.duration,
                                     length=section.length)

            subpaths.append(subpath)
        else:
            print ('[DEBUG]: what to do with this section: '
                   + '{section}'.format(section=section))

    message = message.format(duration=journey.duration,
                             start=format_datetime(journey.start_time),
                             end=format_datetime(journey.end_time),
                             path='\n'.join(subpaths))

    print (message)
    return message
