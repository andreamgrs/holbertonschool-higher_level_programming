#!/usr/bin/python3
import sys
import os


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
my_list = []

if os.path.isfile(filename) is True:
    my_list = load_from_json_file(filename)

for cont in range(1, len(sys.argv)):
    my_list.append(sys.argv[cont])

save_to_json_file(my_list, filename)
