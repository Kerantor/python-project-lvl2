"""Module of rendering to plain format function."""


def convert(value):
    if value is None:
        return 'null'
    elif type(value) is bool:
        return 'true' if value else 'false'
    elif type(value) is dict:
        value = '[complex value]'
    else:
        value = "'{}'".format(value)
    return value


def generate_text(diff_dict, path=''):
    lines = []
    for key, val in sorted(diff_dict.items()):
        current_path = path + key
        flag, value = val
        if flag == 'Nested':
            lines.append(generate_text(
                value, '{}.'.format(
                    current_path)
            ))
        elif flag == 'Changed':
            lines.append(
                "Property '{}' was updated. From {} to {}".format(
                    current_path,
                    convert(value[0]),
                    convert(value[1])
                )
            )
        elif flag == 'Added':
            lines.append(
                "Property '{}' was added with value: {}".format(
                    current_path,
                    convert(value)
                )
            )
        elif flag == 'Removed':
            lines.append(
                "Property '{}' was removed".format(current_path)
            )
    result = ('\n').join(lines)
    return result
