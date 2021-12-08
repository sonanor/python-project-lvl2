import os.path


def get_full_filepath(filepath: str) -> str:
    test_root = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(test_root, 'fixtures', filepath)
