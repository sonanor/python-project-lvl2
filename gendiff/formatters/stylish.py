from gendiff.diff_builder import ChangeStatus, Node


def stylish_result(diff_nodes: list[Node], depth=0):
    result = '{\n'
    indent = '  '
    indent += '    ' * depth
    symbols = {
        ChangeStatus.Added: '+',
        ChangeStatus.Removed: '-',
        ChangeStatus.Unchanged: ' '
    }
    for item in diff_nodes:
        if item.status == ChangeStatus.Nested:
            value = stylish_result(item.children, depth + 1)
            result += f"{indent}  {item.name}: {value}\n"
        elif item.status == ChangeStatus.Changed:
            old_value = format_value(item.old_value, indent)
            new_value = format_value(item.new_value, indent)
            result += f"{indent}{symbols[ChangeStatus.Removed]} {item.name}: {old_value}\n"
            result += f"{indent}{symbols[ChangeStatus.Added]} {item.name}: {new_value}\n"
        else:
            value = format_value(item.value, indent)
            result += f"{indent}{symbols[item.status]} {item.name}: {value}\n"

    result += indent[:-2] + '}'
    return result


def format_value(value, indent):
    result = ''
    if value is True:
        result += 'true'
    elif value is False:
        result += 'false'
    elif value is None:
        result += 'null'
    elif type(value) is dict:
        indent += '    '
        result += '{\n'
        for key in value.keys():
            data = format_value(value[key], indent)
            result += f"{indent}  {key}: {data}\n"
        result += indent[:-2] + '}'
    else:
        result += str(value)
    return result
