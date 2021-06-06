#!/usr/bin/env python


"""Script of the 'Difference Generator'."""


from gendiff.modules import gendiff
from gendiff import cli


def main():
    args = cli.parse_args()
    print(gendiff.generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
