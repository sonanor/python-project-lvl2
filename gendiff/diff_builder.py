def create_inner_diff(before_data, after_data):
    """
    :param before_data: first file in dict representation
    :param after_data: second file in dict representation
    :return: inner representation of diff
    """
    keys = sorted(before_data.keys() | after_data.keys())
    result = []

    for key in keys:
        node = {'name': key}
        before = before_data.get(key)
        after = after_data.get(key)
        if isinstance(before, dict) and isinstance(after, dict):
            node['status'] = 'nested'
            node['children'] = create_inner_diff(before, after)
        elif before is None:
            node['status'] = 'added'
            node['value'] = after_data[key]
        elif after is None:
            node['status'] = 'removed'
            node['value'] = before_data[key]
        elif before == after:
            node['status'] = 'unchanged'
            node['value'] = before_data[key]
        else:
            node['status'] = 'changed'
            node['old_value'] = before_data[key]
            node['new_value'] = after_data[key]
        result.append(node)
    return result
