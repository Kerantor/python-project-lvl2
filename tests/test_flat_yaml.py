"""Flat yaml files test."""


from gendiff import generate_diff


def test_gendiff():
    json1 = "tests/fixtures/flat_json_1.json"
    json2 = "tests/fixtures/flat_yaml.yml"
    right_answer = open(
        "tests/fixtures/expectations/right_flat.txt",
        mode="r",
        encoding="UTF-8"
    )
    assert generate_diff.generate_diff(json1, json2) == right_answer.read()
