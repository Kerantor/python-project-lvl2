import json
import yaml
from gendiff.modules.parsing import parse_diff


def generate_diff(first_file, second_file):
    if str(first_file).endswith('.json'):
        file1 = json.load(open(str(first_file)))
    elif str(first_file).endswith(('.yaml', '.yml')):
        file1 = yaml.safe_load(open(str(first_file)))
    if str(second_file).endswith('.json'):
        file2 = json.load(open(str(second_file)))
    elif str(second_file).endswith(('.yaml', '.yml')):
        file2 = yaml.safe_load(open(str(second_file)))
    result = parse_diff(file1, file2)
    return result
