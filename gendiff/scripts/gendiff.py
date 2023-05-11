#!/usr/bin/env python3
import argparse


parser = argparse.ArgumentParser(
    description='Compares two configuration files and shows a difference.'
    )
parser.add_argument('first_file', type=str)
parser.add_argument('second_file', type=str)


def main():
    return parser.parse_args()
    


if __name__ == '__main__':
    main()
