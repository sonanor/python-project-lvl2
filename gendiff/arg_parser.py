import json
import os

import yaml


def read_file(file: str):
    """Reads file with the help of Parser function which returns dict"""
    with open(file, 'r') as fd:
        file_format = os.path.splitext(file)[1]
        file_content = fd.read()
    return parser(file_format, file_content)


def parser(file_format, file_content) -> dict:
    mapping = {
        '.json': json.loads,
        '.yml': yaml.safe_load,
        '.yaml': yaml.safe_load
    }
    return mapping[file_format](file_content)
