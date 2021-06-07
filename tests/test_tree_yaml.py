"""Tree yaml files test."""


from gendiff.modules import gendiff


def test_gendiff():
    json1 = "tests/fixtures/tree_json_1.json"
    yaml2 = "tests/fixtures/tree_yaml.yml"
    right_answer = open(
        "tests/fixtures/expectations/right_tree.txt"
    )
    assert gendiff.generate_diff(json1, yaml2) == right_answer.read()
