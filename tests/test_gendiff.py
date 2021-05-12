import json
from gendiff.modules.gendiff import generate_diff


def test_gendiff():
    right_answer = json.load(open(str(fixtures.right_answer)))
    assert generate_diff(
        fixtures.json1.json, fixtures.json2.json
    ) == right_answer
