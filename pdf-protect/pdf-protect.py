#!/usr/bin/env python3

import csv
import subprocess

def import_csv(datafile):
    data = []

    try:
        with open(datafile, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for line in reader:
                data.append(line)

    except FileNotFoundError:
        return None

    return data



def parse_arguments():
    import argparse

    desc = 'Password protect a list of pdfs.'
    parser = argparse.ArgumentParser(description=desc)

    # Short Arguments
    parser.add_argument('-a', '--append_string', type=str,
                        default=' (Protected)', metavar='APPEND')

    parser.add_argument('-l', '--list', action='store_true')
    parser.add_argument('-p', '--password', type=str, metavar='PWD')
    parser.add_argument('-v', '--verbose', action='store_true')

    # Positional Arguments
    parser.add_argument('file', metavar='FILE', type=str)

    return parser.parse_args()



def protect_file(filename, output, password=None):
    if password is None:
        password = input('Password: ')

    shell_cmd = ['pdftk']
    shell_cmd.append(filename)
    shell_cmd.append('output')
    shell_cmd.append(output)
    shell_cmd.append('user_pw')
    shell_cmd.append(password)

    subprocess.call(shell_cmd)


def main(args):
    if args.list:
        data = import_csv(args.file)

        for line in data:
            pdf = line['file']
            pwd = line['password']

            protect_file(pdf, pdf + args.append_string, pwd)

    else:
        protect_file(args.file, args.file + args.append_string, args.password)



if __name__ == '__main__':
    args = parse_arguments()
    main(args)
