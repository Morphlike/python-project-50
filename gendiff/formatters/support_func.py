import itertools


def format_value(value):
    if isinstance(value, bool):
        formatted = str(value).lower()
    elif value is None:
        formatted = 'null'
    elif isinstance(value, (int, float)):
        formatted = str(value)
    elif isinstance(value, dict):
        formatted = '[complex value]'
    else:
        formatted = f"'{value}'"
    return formatted


def build_line(key, value, sign, depth):
    indent = ('    ' * depth)
    lines = []

    if isinstance(value, dict):
        dict_lines = []
        for k, v in sorted(value.items()):
            dict_lines.append(build_line(k, v, ' ', depth + 1))

        result = itertools.chain("{", dict_lines, [indent + "    }"])

        line = '\n'.join(result)
        lines.append(f'{indent}  {sign} {key}: {line}')
    else:
        lines.append(f'{indent}  {sign} {key}: {format_value(value)}')
    return '\n'.join(lines)
