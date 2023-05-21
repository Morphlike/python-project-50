from gendiff.diff import open_file
from gendiff.diff import get_diff
from gendiff.diff import make_format


def generate_diff(file_path1, file_path2, format='stylish'):
    data1 = open_file(file_path1)
    data2 = open_file(file_path2)
    diff = get_diff(data1, data2)
    result = make_format(diff, format)
    return result
