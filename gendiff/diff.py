import json
from yaml import safe_load


def get_format(filepath):
    if filepath.endswith('.json'):
        format = 'json'
    elif filepath.endswith('.yaml') or filepath.endswith('.yml'):
        format = 'yaml'
    else:
        format = 'other format'
    return format


def parse_json(filepath):
    with open(filepath, 'r') as filedata:
        data = json.load(filedata)
    return data


def parse_yaml(filepath):
    with open(filepath, 'r') as filedata:
        data = safe_load(filedata)
    return data


def read_file(filepath):
    format = get_format(filepath)

    if format == 'json':
        data = parse_json(filepath)
    elif format == 'yaml':
        data = parse_yaml(filepath)
    else:
        raise Exception('Files should be json or yaml format')
    return data


def get_diff(old_data, new_data):

    def make_key_diff(key):
        value_old = old_data.get(key, None)
        value_new = new_data.get(key, None)
        key_diff = (key, ['unchanged', value_old, value_new, None])

        if key not in old_data:
            key_diff[1][0] = 'added'
        elif key not in new_data:
            key_diff[1][0] = 'removed'
        elif isinstance(value_old, dict) and isinstance(value_new, dict):
            key_diff[1][3] = get_diff(value_old, value_new)
            key_diff[1][1], key_diff[1][2] = [None, None]
        elif value_old != value_new:
            key_diff[1][0] = 'updated'
        else:
            key_diff[1][1] = None
        return key_diff

    unique_keys = sorted(old_data.keys() | new_data.keys())
    diff = list(map(make_key_diff, unique_keys))

    return diff
