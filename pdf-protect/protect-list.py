#!/usr/bin/env python3

import argparse
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



if __name__ == '__main__':
    arg_desc = 'Password protect a list of pdfs.'
    parser = argparse.ArgumentParser(description=arg_desc)

    # Short Arguments
    parser.add_argument('-a', '--append_string', type=str,
                        default=' (Protected)', metavar='APPEND')

    # Positional Arguments
    parser.add_argument('csv_file', metavar='CSV', type=str)

    args = parser.parse_args()

    data = import_csv(args.csv_file)

    for obj in data:
        pdf = obj['file']
        pwd = obj['password']

        shell_cmd = ['pdf-protect.sh']
        shell_cmd.extend(('-p', pwd))
        shell_cmd.extend(('-a', args.append_string))
        shell_cmd.append(pdf)

        subprocess.call(shell_cmd)
