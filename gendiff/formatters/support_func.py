def get_key_name(key_diff):
    return key_diff[0]


def get_status(key_diff):
    return key_diff[1][0]


def get_children(key_diff):
    return key_diff[1][3]


def get_value(key_diff):
    if get_status(key_diff) == 'removed':
        return key_diff[1][1]
    return key_diff[1][2]


def get_old_value(key_diff):
    return key_diff[1][1]


def is_changed_key(key_diff):
    if get_status(key_diff) != 'unchanged' or get_children(key_diff):
        return True
    return False
