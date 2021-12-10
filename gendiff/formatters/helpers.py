from typing import Any


def get_value_repr(value: Any) -> str:
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    return ''
