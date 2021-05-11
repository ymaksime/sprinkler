#!/usr/bin/env python3

import yaml
import logging
from datetime import datetime

parser_logger = logging.getLogger('Parser')

class ProfileParser:
    """This is a class for profile parser.  The idea here is to help to parse
    the irrigation demands stored in YAML frofile files.
    """

    def __init__(self, prof):

        with open(prof, 'r') as profile:
            try:
                temp = yaml.safe_load(profile)
                #t = a['time']
                #dt_object = datetime.strptime(t,"%H:%M:%S")
                #print(datetime.time(dt_object))
            except yaml.YAMLError as exc:
                valve_logger.error('Could not load profile')
                valve_logger.error(exc)

        # Get the ordered jobs dictionary
        self.jobs = self.__sort_jobs(temp)
        # Get the start time
        self.time = self.__parse_start_time(temp)

    def __sort_jobs(self, prof):
        """Sort the given profile based on the required irrigation time"""
        sorted_jobs = {}
        for item in prof:
            # YAML frofile contains not just info for each irrigation branch
            if 'branch' in item:
                # Just as a pre-causion, do not allow dublicates
                if item not in sorted_jobs:
                    # This dicrionary is still unsorted
                    sorted_jobs[item] = prof.get(item)

        # Sort the dictionary by the to time required to irrigate
        return sorted(sorted_jobs.items(), key=lambda x: x[0])

    def __parse_start_time(self, prof):
        """Private method which parsers the time_bigin entry in the YAML file"""
        t = prof['time_begin']
        dt_object = datetime.strptime(t,"%H:%M:%S")
        return datetime.time(dt_object)

    def get_time(self):
        """Returns back a datetime object with the execution start time"""
        return self.time

    def get_jobs(self):
        """Returns the sorted dictionary of all jobs for the current profile"""
        return self.jobs

    def info(self):
        """Prints out the content of all internal dictionaries"""
        parser_logger.info(self.time)
        parser_logger.info(self.jobs)
