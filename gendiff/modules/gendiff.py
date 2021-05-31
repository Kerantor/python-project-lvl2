from gendiff.modules.parsing import parse_diff
from gendiff.formatters import FORMATTER
import yaml
import json


def extract_data(file):
    if str(file).endswith('.json'):
        result = json.load(open(str(file)))
    elif str(file).endswith(('.yaml', '.yml')):
        result = yaml.safe_load(open(str(file)))
    return result


def generate_diff(first_file, second_file, output_format='stylish'):
    file1 = extract_data(first_file)
    file2 = extract_data(second_file)
    formatter = FORMATTER[output_format]
    result = formatter(parse_diff(file1, file2))
    return result
