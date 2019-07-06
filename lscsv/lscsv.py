#!/usr/bin/env python3

def list_files(directory):
    import os

    _, _, filelist = next(os.walk(directory))

    for file in filelist:
        print(file)



def parse_arguments():
    """ Parses Command Line arguments """
    import argparse

    parser = argparse.ArgumentParser(description="""Creates a csv containing
    filenames in the specified directory.""")

    # Positional Arguments
    parser.add_argument('directory', metavar='DIR', type=str)

    return parser.parse_args()



def main(args):
    list_files(args.directory)



if __name__ == '__main__':
    CLI_ARGS = parse_arguments()
    main(CLI_ARGS)
