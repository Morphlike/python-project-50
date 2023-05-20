from gendiff.formatters.support_func import format_value

def get_plain(data):
    result = plain(data)
    return result


def plain(items, path=''):
    lines = []
    items.sort(key=lambda item: item['key'])

    for item in items:
        if path:
            absolute_path = f"{path}.{item['key']}"

        else:
            absolute_path = item['key']

        if item['action'] == 'old_key':
            lines.append(f"Property '{absolute_path}' was removed")

        elif item['action'] == 'new_key':
            lines.append(
                f"Property '{absolute_path}' was added "
                f"with value: {format_value(item['new_value'])}")

        elif item['action'] == 'new_value':
            lines.append(
                f"Property '{absolute_path}' was updated. "
                f"From {format_value(item['old_value'])} "
                f"to {format_value(item['new_value'])}")

        elif item['action'] == 'parent':
            lines.append(plain(item['child'], absolute_path))

    '\n'.join(lines)
    return '\n'.join(lines)
