def generate_text(sign, key, value):
    result = "  {} {}: {}\n".format(sign, key, value)
    return result


def parse_diff(first_file, second_file):
    all_keys = first_file.keys() | second_file.keys()
    result = '{' + '\n'
    for i in sorted(all_keys):
        if i in first_file.keys():
            if i in second_file.keys():
                if first_file[i] == second_file[i]:
                    result = result + generate_text(' ', i, str(first_file[i]))
                else:
                    result = result + generate_text('-', i, str(first_file[i]))
                    result = result + generate_text('+', i, str(second_file[i]))
            else:
                result = result + generate_text('-', i, str(first_file[i]))
        else:
            result = result + generate_text('+', i, str(second_file[i]))
    result = result + '}'
    return result
