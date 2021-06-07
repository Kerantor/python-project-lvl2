"""Module of extracting data from files."""


import yaml
import json


def extract_data(file):
    if str(file).endswith('.json'):
        result = json.load(open(str(file)))
    elif str(file).endswith(('.yaml', '.yml')):
        result = yaml.safe_load(open(str(file)))
    return result
