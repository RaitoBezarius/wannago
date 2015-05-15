from data import Journey

def report_journey(api, from_place, to_place, without=None):
    resp = api.compute_journey(from_place, to_place)
    journey = Journey(resp['journeys'][0])

    message = '[{duration} mn]\n{path}'
    subpaths = []
    for section in journey.sections:
        if section.type == 'public_transport':
            subpath = '==> {net_label} - {to_place} [{duration} mn]'.\
            format(net_label=section.network_label, from_place=section.from_section.name,
                   to_place=section.to_section.name,
                   duration=section.duration)
            subpaths.append(subpath)
        else:
            print ('[DEBUG]: what to do with this section: {section}'.format(section=section))

    message = message.format(duration=journey.duration, path='\n'.join(subpaths))

    print (message)
