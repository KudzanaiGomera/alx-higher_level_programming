#!/usr/bin/python3

"""
Add arguments to a list, then save those arguments to a file
"""

import sys
import os.path


args = sys.argv[1:]

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

new = []
if os.path.exists("./add_item.json"):
    new = load_from_json_file("add_item.json")

save_to_json_file(new + args, "add_item.json")
