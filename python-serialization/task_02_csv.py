#!/usr/bin/env python3
import csv
import json


def convert_csv_to_json(filename_csv):
    my_dict = []
    try:
        with open(filename_csv, mode="r", encoding="utf-8") as file:
            new_dict = csv.DictReader(file)
            for row in new_dict:
                my_dict.append(row)
    except FileNotFoundError:
        return False

    json_str = json.dumps(my_dict)

    try:
        with open("data.json", mode="w", encoding="utf-8") as json_file:
            json_file.write(json_str)
            return True
    except FileNotFoundError:
        return False
