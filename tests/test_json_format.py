"""Json format test."""


from gendiff import generate_diff
import json


def test_gendiff():
    json1 = "tests/fixtures/tree_json_1.json"
    json2 = "tests/fixtures/tree_json_2.json"
    right_answer = json.load(open(
        "tests/fixtures/expectations/right_json.json"
    ))
    assert json.loads(
        generate_diff.generate_diff(
            json1, json2, 'json'
        )
    ) == right_answer
