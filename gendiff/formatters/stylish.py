from itertools import chain
from gendiff.formatters.support_func import build_line


def get_stylish(items, depth=0):
    lines = []
    indent = '    ' * depth
    items.sort(key=lambda item: item['key'])
    for item in items:
        if item['action'] == 'old_key':
            lines.append(build_line(item['key'], item['old_value'], '-', depth))

        elif item['action'] == 'new_key':
            lines.append(build_line(item['key'], item['new_value'], '+', depth))

        elif item['action'] == 'no_changes':
            lines.append(build_line(item['key'], item['old_value'], ' ', depth))

        elif item['action'] == 'new_value':
            lines.append(build_line(item['key'], item['old_value'], '-', depth))
            lines.append(build_line(item['key'], item['new_value'], '+', depth))

        elif item['action'] == 'parent':
            lines.append(
                f"{indent}    {item['key']}:"
                f" {get_stylish(item['child'], depth+1)}"
            )

    result = chain("{", lines, [indent + "}"])
    final = '\n'.join(result)
    return final
