import json
from gendiff.modules.gendiff import generate_diff


def test_gendiff():
    json1 = "tests/fixtures/json1.json"
    json2 = "tests/fixtures/json2.json"
    right_answer = "tests/fixtures/right_answer.json"
    assert generate_diff(json1, json2) == json.load(open(str(right_answer)))
