#!/usr/bin/env python


"""Script of the 'Difference Generator'."""


from gendiff import generate_diff
from gendiff import cli


def main():
    args = cli.parse_args()
    print(
        generate_diff.generate_diff(
            args.first_file,
            args.second_file,
            args.format
        )
    )


if __name__ == '__main__':
    main()
