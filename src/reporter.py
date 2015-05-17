from data import Journey

def format_color(hexa, message):
    """
    Please, better function, please. This is just a PoC done between two hour
    of school.
    """
    r, g, b = int(hexa[0:2], 16), int(hexa[2:4], 16), int(hexa[4:6], 16)

    escape_character = '\033[38;5;{fgcode}m'.format(fgcode=16 + 36 * r + b)

    return '{color}{message}{reset}'.format(color=escape_character,
            message=message,
            reset='\033[0;00m')

def report_journey(api, from_place, to_place, without=None):
    resp = api.compute_journey(from_place, to_place)
    journey = Journey(resp['journeys'][0])

    message = '[{duration} mn] - [{start_hour}h{start_minutes}]\n{path}\n[{end_hour}h{end_minutes}]'
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
            start_hour=journey.start_time.format('HH'),
            start_minutes=journey.start_time.format('mm'),
            end_hour=journey.end_time.format('HH'),
            end_minutes=journey.end_time.format('mm'),
            path='\n'.join(subpaths))

    print (message)
    return message
