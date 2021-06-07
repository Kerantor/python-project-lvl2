"""Tree yaml files test."""


from gendiff import generate_diff


def test_gendiff():
    json1 = "tests/fixtures/tree_json_1.json"
    yaml2 = "tests/fixtures/tree_yaml.yml"
    right_answer = open(
        "tests/fixtures/expectations/right_tree.txt"
    )
    assert generate_diff.generate_diff(json1, yaml2) == right_answer.read()
