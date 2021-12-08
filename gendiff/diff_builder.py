import enum
from dataclasses import dataclass
from typing import Union, Optional


class ChangeStatus(enum.Enum):
    Added = 1
    Removed = 2
    Nested = 3
    Changed = 4
    Unchanged = 5


@dataclass
class Node:
    name: str
    status: Optional[ChangeStatus] = None
    children: Optional[list] = None
    value: Optional[Union[str, dict]] = None
    old_value: Optional[Union[str, dict]] = None
    new_value: Optional[Union[str, dict]] = None


def create_diff(before_data: dict, after_data: dict) -> list[Node]:
    """
    Create list of dicts - difference between two strings.

    :param before_data: first file in dict representation
    :param after_data: second file in dict representation
    :return: inner representation of diff
    """
    keys: list[str] = sorted(before_data.keys() | after_data.keys())
    result = []

    for key in keys:
        node = Node(name=key)
        elem_before = before_data.get(key)
        elem_after = after_data.get(key)
        if isinstance(elem_before, dict) and isinstance(elem_after, dict):
            node.status = ChangeStatus.Nested
            node.children = create_diff(elem_before, elem_after)
        elif elem_before is None:
            node.status = ChangeStatus.Added
            node.value = after_data[key]
        elif elem_after is None:
            node.status = ChangeStatus.Removed
            node.value = before_data[key]
        elif elem_before == elem_after:
            node.status = ChangeStatus.Unchanged
            node.value = before_data[key]
        else:
            node.status = ChangeStatus.Changed
            node.old_value = before_data[key]
            node.new_value = after_data[key]
        result.append(node)
    return result
