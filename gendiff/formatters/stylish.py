SYMBOLS = {
    'added': '+ ',
    'removed': '- ',
    'unchanged': ' ',
    'nested': ' {\n '
}


def stylish_result(diff_inner_repr, depth=0):
    result = '{\n'
    indent = '  '
    for _ in range(depth):
        indent += '    '
    for item in diff_inner_repr:
        if item['status'] == 'nested':
            data = stylish_result(item['children'], depth + 1)
            result += f"{indent}  {item['name']}: {data}\n"
        elif item['status'] == 'changed':
            result += f"{indent}- {item['name']}: {format_value(item['old_value'], indent)}\n"
            result += f"{indent}+ {item['name']}: {format_value(item['new_value'], indent)}\n"
        elif item['status'] == 'added':
            result += f"{indent}+ {item['name']}: {format_value(item['value'], indent)}\n"
        elif item['status'] == 'removed':
            result += f"{indent}- {item['name']}: {format_value(item['value'], indent)}\n"
        elif item['status'] == 'unchanged':
            result += f"{indent}  {item['name']}: {format_value(item['value'], indent)}\n"
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
