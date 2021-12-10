from gendiff.diff_builder import Node, ChangeStatus
from gendiff.formatters.helpers import get_value_repr


def plain_result(diff_nodes: list[Node]) -> str:
    return _plain_result(diff_nodes).removesuffix('\n')


def _plain_result(diff_nodes: list[Node], parent=None) -> str:
    result = ''
    for item in diff_nodes:
        if item.status == ChangeStatus.Unchanged:
            continue
        name = f'{parent}.{item.name}' if parent else item.name
        if item.status == ChangeStatus.Nested:
            result += _plain_result(item.children, name)
        else:
            result += f'Property {format_value(name)} {get_status_output(item)}\n'
    return result


def get_status_output(node: Node) -> str:
    if node.status == ChangeStatus.Added:
        return f'was added with value: {format_value(node.value)}'
    if node.status == ChangeStatus.Removed:
        return 'was removed'
    if node.status == ChangeStatus.Changed:
        return f'was updated. From {format_value(node.old_value)} to {format_value(node.new_value)}'


def format_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    if value_repr := get_value_repr(value):
        return value_repr
    else:
        return f"'{str(value)}'"
