"""Formattes package."""


from gendiff.formatters import stylish, plain, json

FORMATTER = {
    'stylish': stylish.generate_text,
    'plain': plain.generate_text,
    'json': json.generate_text,
}
