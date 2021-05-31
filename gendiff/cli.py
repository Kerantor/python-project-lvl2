import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        description='Generate diff.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format',
        choices=['plain', 'json', 'stylish'],
        metavar='FORMAT',
        help='set format of output',
        dest='format',
        default='stylish'
    )
    return parser.parse_args()
