import json


def generate_diff(first_file, second_file):
    json1 = json.load(open(str(first_file)))
    json2 = json.load(open(str(second_file)))
    all_keys = json1.keys() | json2.keys()
    result = '{' + '\n'
    for i in sorted(all_keys):
        if i in json1.keys():
            if i in json2.keys():
                if json1[i] == json2[i]:
                    result = result + '    ' + i + ':' + str(json1[i]) + '\n'
                else:
                    result = result + '  - ' + i + ':' + str(json1[i]) + '\n'
                    result = result + '  + ' + i + ':' + str(json2[i]) + '\n'
            else:
                result = result + '  - ' + i + ':' + str(json1[i]) + '\n'
        else:
            result = result + '  + ' + i + ':' + str(json2[i]) + '\n'
    result = result + '}'
    return result
