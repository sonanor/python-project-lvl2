from .stylish import stylish_result


def create_output_result(diff_data: list, output_format: str):
    if output_format == 'stylish':
        return stylish_result(diff_data)
