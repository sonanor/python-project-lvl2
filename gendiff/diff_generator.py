from .arg_parser import parse_file
from .diff_builder import create_diff
from .formatters.format_output import create_output_result


def generate_diff(first_path: str, second_path: str, output_format='stylish') -> str:
    first_file_dict = parse_file(first_path)
    second_file_dict = parse_file(second_path)
    diff = create_diff(first_file_dict, second_file_dict)
    output = create_output_result(diff, output_format)
    return output
