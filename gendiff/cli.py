#!/usr/bin/env python3
import argparse
import json
import yaml


def parse_args():
    parser = argparse.ArgumentParser(
    description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', type=str,
                    help='set format of output(default: "stylish)')
    args = parser.parse_args()
    return args.first_file, args.second_file, args.format


def parcing_files(file_path1, file_path2):
    file_paths = (file_path1, file_path2)
    files = []
    for file_path in file_paths:
        if '.json' in file_path:
            file = json.load(open(file_path))
        elif '.yml' or '.yaml' in file_path:
            file = yaml.load(open(file_path), Loader=yaml.SafeLoader)
        files.append(file)
    return files
