# coding: utf8

import argparse
import requests
from transport import initialize_api
from reporter import report_journey

def try_get_current_place():
    return None

def handle_coverage_switching(args):
    raise NotImplemented

def handle_journey_computing(args):
    from_place = args.from_place or try_get_current_place()
    report_journey(args.api, from_place, args.place)

def handle_location_managing(args):
    raise NotImplemented

def subcommand(func):
    def wrap(f):
        def setup_subcommand(subparser):
            parser = f(subparser)
            parser.set_defaults(func=func)
        return setup_subcommand
    return wrap

@subcommand(handle_coverage_switching)
def enable_coverage_switcher(parser):
    coverage_switcher = parser.add_parser('switch', help='Coverage zone switch help')
    coverage_switcher.add_argument('zone', type=str, choices=['fr-idf'], help='The new zone where the system will work')
    return coverage_switcher

@subcommand(handle_journey_computing)
def enable_journey_computer(parser):
    journey_computer = parser.add_parser('to', help='Journey help')
    journey_computer.add_argument('place', type=str, help='The location where you want to go')
    journey_computer.add_argument('--from', type=str, default=None,
                                  dest="from_place",
                                  help="""The location from you want to go,
                                    by default, it will tries to find it from your internet connection otherwise,
                                    it will check if there is a default from place, and get it.
                                    If no place can be found, the program will display a error message and exits with error status code 1.""")
    journey_computer.add_argument('--without', type=str, default=None,
                                  help="Which public transports do you want to skip in your journey? (e.g. Bus, Metro, RER)")
    return journey_computer

@subcommand(handle_location_managing)
def enable_location_manager(parser):
    location_manager = parser.add_parser('save', help='Location saving help')
    location_manager.add_argument('place', help='The place which you want to save')
    location_manager.add_argument('name', help='The name you want to give to this place (e.g home, school, work)')
    return location_manager


def main():
    parser = argparse.ArgumentParser(prog='wannago',
                                     formatter_class=argparse.RawTextHelpFormatter,
                                     description='Give you the movement list of your character from point A to point B in oneshot !')

    parser.add_argument('--token', help='API key for Navitia.io')
    command_subparsers = parser.add_subparsers(help='sub-commands help')

    subcommands = [enable_coverage_switcher,
     enable_journey_computer,
     enable_location_manager]

    for subcommand_init in subcommands:
        subcommand_init(command_subparsers)

    args = parser.parse_args()
    API_KEY = "INSERT_YOUR_API_KEY_HERE"
    api = initialize_api(args.token or API_KEY)
    args.api = api
    args.func(args)

if __name__ == '__main__':
    main()
