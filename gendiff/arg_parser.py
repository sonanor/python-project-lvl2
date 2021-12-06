import json
import os

import yaml


def parser(file):
    file_format = os.path.splitext(file)[1]
    result = {}
    if file_format == '.yaml' or file_format == '.yml':
        with open(file) as fd:
            result = yaml.safe_load(fd)
    elif file_format == '.json':
        result = json.load(open(file, 'r'))
    return result
