import pytest

from gendiff.diff_generator import generate_diff
from tests.conftest import get_full_filepath
from tests.expected_result import SIMPLE_STRING, RECURSIVE_STILISH


@pytest.mark.parametrize(
    'first_path, second_path, expected',
    [
        ['json_files/simple_1.json', 'json_files/simple_2.json', SIMPLE_STRING],
        ['yml_files/simple_1.yml', 'yml_files/simple_2.yml', SIMPLE_STRING],
        ['json_files/recursive_1.json', 'json_files/recursive_2.json', RECURSIVE_STILISH],
        ['yml_files/recursive_1.yml', 'yml_files/recursive_2.yml', RECURSIVE_STILISH],
    ],
    ids=[
        'simple_case_json', 'simple_case_yaml',
        'recursive_case_json', 'recursive_case_yaml'
    ]
)
def test_gendiff(first_path: str, second_path: str, expected: str):
    assert generate_diff(
        get_full_filepath(first_path),
        get_full_filepath(second_path)
    ) == expected
