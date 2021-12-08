#!/usr/bin/env python

from .arg_parser import read_file
from .diff_builder import create_inner_diff
from gendiff.formatters.format_output import create_output_result


def generate_diff(first_path: str, second_path: str, output_format='stylish'):
    first_file_dict = read_file(first_path)
    second_file_dict = read_file(second_path)
    diff_inner_repr = create_inner_diff(first_file_dict, second_file_dict)
    output = create_output_result(diff_inner_repr, output_format)
    return output
    # getting and formatting difference
    # first_set = set(first_file_dict.items())
    # second_set = set(first_file_dict.items())
    #
    # common = first_set & second_set
    # common_formated = {(key, value, 0) for key, value in common}
    # first_only = first_set - second_set
    # first_formated = {(key, value, 1) for key, value in first_only}
    # second_only = second_set - first_set
    # second_formated = {(key, value, 2) for key, value in second_only}
    #
    # # sorting and returning result
    # merged_list = list(common_formated | first_formated | second_formated)
    # sorted_list = sorted(merged_list, key=lambda x: (x[0], x[2]))
    # symbols = [' ', '-', '+']
    # output = []
    # for key, value, flag in sorted_list:
    #     output.append(f'  {symbols[flag]} {key}: {value}')
    # return '{\n' + '\n'.join(output) + '\n}'

