from gendiff.diff_generator import generate_diff
from tests import expected_result


def test1_simple_case():
    expected = expected_result.SIMPLE_STRING
    assert generate_diff('tests/fixtures/json_files/simple_1.json',
                         'tests/fixtures/json_files/simple_2.json') == expected
    assert generate_diff('tests/fixtures/yml_files/simple_1.yml',
                         'tests/fixtures/yml_files/simple_2.yml') == expected


def test2_recursive_case():
    expected = expected_result.RECURSIVE_STILISH_JSON
    assert generate_diff('tests/fixtures/json_files/recursive_1.json',
                         'tests/fixtures/json_files/recursive_2.json') == expected
    assert generate_diff('tests/fixtures/yml_files/recursive_1.yml',
                         'tests/fixtures/yml_files/recursive_2.yml') == expected
