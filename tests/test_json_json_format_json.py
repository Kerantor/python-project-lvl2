from gendiff.modules.gendiff import generate_diff
import json


def test_gendiff():
    json1 = "tests/fixtures/json2-1.json"
    json2 = "tests/fixtures/json2-2.json"
    right_answer = json.load(open('tests/fixtures/right_json.json'))
    assert json.loads(generate_diff(json1, json2, 'json')) == right_answer
