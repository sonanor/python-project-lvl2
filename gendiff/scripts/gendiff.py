from gendiff.diff_generator import generate_diff


def main():
    import argparse

    choices_format = ['stylish', 'plain', 'json']
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', action='store',
                        default='stylish', choices=choices_format, help='set format of output')
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file, args.format.lower())
    print(diff)


if __name__ == '__main__':
    main()
