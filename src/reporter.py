from data import Journey
from color import format_color

def report_journey(api, from_place, to_place, without=None):
    resp = api.compute_journey(from_place, to_place)
    journey = Journey(resp['journeys'][0])

    message = '[{duration} mn] - [{start}]\n{path}\n[{end}]'
    subpaths = []
    for section in journey.sections:
        if section.type == 'public_transport':
            subpath = '==> {net_label} - {to_place} [{duration} mn]'.\
            format(net_label=section.network_label,
                   to_place=section.to_section.name,
                   duration=section.duration)
            if section.has_color:
                subpath = format_color(section.color, subpath)

            subpaths.append(subpath)
        else:
            print ('[DEBUG]: what to do with this section: {section}'.format(section=section))

    message = message.format(duration=journey.duration,
            start=journey.start_time.format('HH:mm:ss'),
            end=journey.end_time.format('HH:mm:ss'),
            path='\n'.join(subpaths))

    print (message)
    return message
