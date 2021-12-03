from gendiff.diff_generator import generate_diff


def test_simple_case():
    expected = open('tests/fixtures/simple_result.txt').read()
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json') == expected
