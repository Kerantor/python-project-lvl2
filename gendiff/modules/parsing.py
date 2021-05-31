def parse_diff(first_file, second_file):
    shared_keys = first_file.keys() & second_file.keys()
    old_keys = first_file.keys() - second_file.keys()
    new_keys = second_file.keys() - first_file.keys()
    result = {}
    for i in old_keys:
        result[i] = ('Removed', first_file[i])
    for i in new_keys:
        result[i] = ('Added', second_file[i])
    for i in shared_keys:
        if first_file[i] == second_file[i]:
            result[i] = ('Unchanged', first_file[i])
        elif type(first_file[i]) is dict and type(second_file[i]) is dict:
            result[i] = ('Nested', parse_diff(first_file[i], second_file[i]))
        else:
            result[i] = ('Changed', (first_file[i], second_file[i]))
    return result
