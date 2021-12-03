from gendiff.diff_generator import generate_diff


def test_simple_case():
    expected = open('fixtures/simple_result.txt').read()
    assert generate_diff('./fixtures/file1.json', './fixtures/file2.json') == expected
