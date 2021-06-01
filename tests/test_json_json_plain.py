from gendiff.modules.gendiff import generate_diff


def test_gendiff():  # noqa: W291
    json1 = "tests/fixtures/json2-1.json"
    json2 = "tests/fixtures/json2-2.json"
    right_answer = """Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]"""  # noqa: W291
    assert generate_diff(json1, json2, 'plain') == right_answer
