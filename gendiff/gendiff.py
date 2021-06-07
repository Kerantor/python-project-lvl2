"""Module of generate diff dict."""


from gendiff.modules.parsing import parse_diff
from gendiff.formatters import FORMATTER
from gendiff.modules.extracting_data import extract_data


def generate_diff(first_file, second_file, output_format='stylish'):
    file1 = extract_data(first_file)
    file2 = extract_data(second_file)
    formatter = FORMATTER[str(output_format)]
    result = formatter(parse_diff(file1, file2))
    return result
