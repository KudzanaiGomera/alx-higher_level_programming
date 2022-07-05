#!/usr/bin/python3

"""
save_to_json_file Module
"""

import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to the text file by using JSON"""
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
