import json
import yaml
from gendiff.formatters.json import get_json
from gendiff.formatters.plain import get_plain
from gendiff.formatters.stylish import get_stylish


def open_file(filepath):
    with open(filepath, 'r') as f:
        return parse_file(f, filepath)


def parse_file(data, filepath):
    if filepath.endswith('.json'):
        return json.load(data)
    elif filepath.endswith('.yaml') or filepath.endswith('.yml'):
        return yaml.safe_load(data)
    else:
        raise ValueError('Unsupported file format')


def get_diff(old_data, new_data):
    keys = sorted(set(old_data.keys()) | set(new_data.keys()))
    result = []
    for key in keys:
        diff_result = {'key': key}

        if key not in new_data.keys():
            diff_result['action'] = 'old_key'
            diff_result['old_value'] = old_data[key]

        elif key not in old_data.keys():
            diff_result['action'] = 'new_key'
            diff_result['new_value'] = new_data[key]

        elif old_data[key] == new_data[key]:
            diff_result['action'] = 'no_changes'
            diff_result['old_value'] = old_data[key]

        elif isinstance(old_data[key], dict) \
                and isinstance(new_data[key], dict):
            diff_result['action'] = 'parent'
            diff_result['child'] = get_diff(old_data[key], new_data[key])

        else:
            diff_result['action'] = 'new_value'
            diff_result['old_value'] = old_data[key]
            diff_result['new_value'] = new_data[key]
        result.append(diff_result)
    return result


def make_format(diff, format):
    if format == 'stylish':
        return get_stylish(diff)
    elif format == 'plain':
        return get_plain(diff)
    elif format == 'json':
        return get_json(diff)
