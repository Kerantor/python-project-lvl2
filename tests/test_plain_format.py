"""Plain format test."""


from gendiff.modules import gendiff


def test_gendiff():
    json1 = "tests/fixtures/tree_json_1.json"
    json2 = "tests/fixtures/tree_json_2.json"
    right_answer = open(
        "tests/fixtures/expectations/right_plain.txt"
    )
    assert gendiff.generate_diff(json1, json2, 'plain') == right_answer.read()
