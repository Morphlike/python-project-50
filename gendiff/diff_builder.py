from gendiff.diff import read_file
from gendiff.diff import get_diff
from gendiff.formatters.json import get_json
from gendiff.formatters.plain import get_plain
from gendiff.formatters.stylish import get_stylish


def generate_diff(file_path1, file_path2, format='stylish'):
    first_file = read_file(file_path1)
    second_file = read_file(file_path2)

    diff = get_diff(first_file, second_file)
    if format == 'plain':
        result = get_plain(diff)
    elif format == 'json':
        result = get_json(diff)
    elif format == 'stylish':
        result = get_stylish(diff)
    else:
        raise Exception('Unsupported format')

    return result
