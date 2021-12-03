#!/usr/bin/env python

import json


def generate_diff(first, second):
    # open files
    first = json.load(open(first, 'r'))
    second = json.load(open(second, 'r'))

    # getting and formatting difference
    first_set = set(first.items())
    second_set = set(second.items())
    common = first_set & second_set
    common_formated = {(key, value, 0) for key, value in common}
    first_only = first_set - second_set
    first_formated = {(key, value, 1) for key, value in first_only}
    second_only = second_set - first_set
    second_formated = {(key, value, 2) for key, value in second_only}

    # sorting and returning result
    merged_list = list(common_formated | first_formated | second_formated)
    sorted_list = sorted(merged_list, key=lambda x: (x[0], x[2]))
    symbols = [' ', '-', '+']
    output = []
    for key, value, flag in sorted_list:
        output.append(f'  {symbols[flag]} {key}: {value}')
    return '{\n' + '\n'.join(output) + '\n}'


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == '__main__':
    main()
