"""Flat json files test."""


from gendiff.modules.gendiff import generate_diff


def test_gendiff():
    json1 = "tests/fixtures/flat_json_1.json"
    json2 = "tests/fixtures/flat_json_2.json"
    right_answer = open(
        "tests/fixtures/expectations/right_flat.txt"
    )
    assert generate_diff(json1, json2) == right_answer.read()
