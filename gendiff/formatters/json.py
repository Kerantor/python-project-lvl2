"""Module of rendering to json format function."""


import json


def generate_text(diff_dict):
    return json.dumps(
        diff_dict,
        indent='    ',
        ensure_ascii=False,
        sort_keys=True
    )
