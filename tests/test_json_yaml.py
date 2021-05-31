from gendiff.modules.gendiff import generate_diff


def test_gendiff():
    json1 = "tests/fixtures/json1.json"
    json2 = "tests/fixtures/yaml2.yml"
    right_answer = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""
    assert generate_diff(json1, json2) == right_answer
