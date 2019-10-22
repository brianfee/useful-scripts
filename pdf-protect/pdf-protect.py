#!/usr/bin/env python3
# pylint: disable=invalid-name
""" This script uses the pdftk program to protect PDFs. """

import subprocess

def import_csv(datafile):
    """ Loads a csv into a dictionary. """

    import csv
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
    """ Parse command line arguments. """

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
    """ Checks for necessary data and password protects PDF using pdftk. """

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
    """ The main pdf-protect function. """

    if args.list:
        data = import_csv(args.file)

        for line in data:
            pdf = line['file']
            output = pdf.replace('.pdf', '') + args.append_string + '.pdf'
            pwd = line['password']
            protect_file(pdf, output, pwd)

            if args.verbose:
                print(pdf + ' -> ' + output)

    else:
        output = args.file.replace('.pdf', '') + args.append_string + '.pdf'
        protect_file(args.file, output, args.password)
        if args.verbose:
            print(args.file + ' -> ' + output)



if __name__ == '__main__':
    main(parse_arguments())
