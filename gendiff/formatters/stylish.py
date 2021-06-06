"""Module of rendering to JSON-like format function."""


_SYMBOLS = {
    'Added': '+',
    'Removed': '-',
    'Unchanged': ' ',
    'Nested': ' ',
}


def convert(value):
    if value is None:
        return 'null'
    elif type(value) is bool:
        return 'true' if value else 'false'
    return value


def join_str(flag, key, value, mult):
    symbol = _SYMBOLS[flag]
    if type(value) is dict:
        normalize_value = generate_text(value, mult + 1)
    else:
        normalize_value = convert(value)
    result = '  {} {}: {}'.format(symbol, key, normalize_value)
    return result


def generate_text(diff_dict, mult=0):
    res_str = []
    result = ''
    for key, val in sorted(diff_dict.items()):
        if type(val) is tuple:
            flag = val[0]
            value = val[1]
        else:
            flag = 'Unchanged'
            value = val

        if flag == 'Nested':
            nested_diff = generate_text(value, mult + 1)
            res_str.append(join_str(flag, key, nested_diff, mult))
        elif flag == 'Changed':
            res_str.append(join_str('Removed', key, value[0], mult))
            res_str.append(join_str('Added', key, value[1], mult))
        else:
            res_str.append(join_str(flag, key, value, mult))
    indent = '{}{}'.format('\n', '    ' * mult)
    result = "{{{0}{1}{2}}}".format(indent, indent.join(res_str), indent)
    return result
