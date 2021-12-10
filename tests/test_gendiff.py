import pytest

from gendiff.diff_generator import generate_diff
from tests.conftest import get_full_filepath
from tests.expected_result import SIMPLE_STYLISH, RECURSIVE_STYLISH, RECURSIVE_PLAIN, SIMPLE_PLAIN


@pytest.mark.parametrize(
    'first_path, second_path, expected, formatter',
    [
        ['json_files/simple_1.json', 'json_files/simple_2.json', SIMPLE_STYLISH, 'stylish'],
        ['yml_files/simple_1.yml', 'yml_files/simple_2.yml', SIMPLE_STYLISH, 'stylish'],
        ['json_files/simple_1.json', 'json_files/simple_2.json', SIMPLE_PLAIN, 'plain'],
        ['yml_files/simple_1.yml', 'yml_files/simple_2.yml', SIMPLE_PLAIN, 'plain'],
        ['json_files/recursive_1.json', 'json_files/recursive_2.json', RECURSIVE_STYLISH, 'stylish'],
        ['yml_files/recursive_1.yml', 'yml_files/recursive_2.yml', RECURSIVE_STYLISH, 'stylish'],
        ['json_files/recursive_1.json', 'json_files/recursive_2.json', RECURSIVE_PLAIN, 'plain'],
        ['yml_files/recursive_1.yml', 'yml_files/recursive_2.yml', RECURSIVE_PLAIN, 'plain'],
    ],
    ids=[
        'simple_stylish_json',
        'simple_stylish_yaml',
        'simple_plain_json',
        'simple_plain_yaml',
        'recursive_stylish_json',
        'recursive_stylish_yaml',
        'recursive_plain_json',
        'recursive_plain_yaml',
    ]
)
def test_gendiff(first_path: str, second_path: str, expected: str, formatter: str):
    assert generate_diff(
        get_full_filepath(first_path),
        get_full_filepath(second_path),
        formatter
    ) == expected
