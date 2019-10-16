#!/usr/bin/python3
import sys
import json

load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file


try:
    list9 = load_from_json_file("add_item.json")
except:
    list9 = []
for i in range(1, len(sys.argv)):
    list9.append(sys.argv[i])

save_to_json_file(list9, "add_item.json")
