#!/usr/bin/python3

"""
load_from_json_file module
"""

import json


def load_from_json_file(filename):
    """Creates an Object from a JSON file"""
    with open(filename, 'r') as f:
        return json.load(f)
