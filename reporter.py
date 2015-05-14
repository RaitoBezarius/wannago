from data import Journey

def report_journey(api, from_place, to_place, without=None):
    resp = api.compute_journey(from_place, to_place)
    journey = Journey(resp['journeys'][0])

    message = '[{duration} minutes] Current => {path}'
    subpaths = []
    for section in journey.sections:
        if section.type == 'public_transport':
            print (section)
            subpath = '{net_label} - {from_place} => {to_place} [{duration} minutes]'.\
            format(net_label=section.network_label, from_place=section.from_section.name,
                   to_place=section.to_section.name,
                   duration=section.duration)
            subpaths.append(subpath)
        else:
            print ('what to do with this section: {section}'.format(section=section))

    message = message.format(duration=journey.duration, path=' ==> '.join(subpaths))

    print (message)
