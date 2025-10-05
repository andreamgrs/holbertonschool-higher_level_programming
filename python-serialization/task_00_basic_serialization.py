#!/usr/bin/env python3
import json


def serialize_and_save_to_file(data, filename):
    # Code here to serialize and save data to the specified file
    with open(filename, "w", encoding="utf-8") as file:
        return json.dump(data, file)


def load_and_deserialize(filename):
    # Code here to load and deserialize data from the specified file
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
