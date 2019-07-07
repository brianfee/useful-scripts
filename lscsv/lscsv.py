#!/usr/bin/env python3
""" Creates a CSV containing a list of files in the specified directory. """

def create_filelist(directory):
    """ Generates a list of files within a given directory. """
    import os

    _, _, filelist = next(os.walk(directory))
    return filelist



def parse_arguments():
    """ Parses Command Line arguments. """
    import argparse

    parser = argparse.ArgumentParser(description="""Creates a CSV containing
                a list of files in the specified directory.""")

    # Positional Arguments
    parser.add_argument('directory', metavar='DIR', type=str)

    return parser.parse_args()



def create_csv_from_list(data, output_file):
    """ Takes a list of data and exports it to a given output file. """
    import pandas as pd
    df = pd.DataFrame(data, columns=['file'])
    df.to_csv(output_file, index=False)



def main(args):
    """ Takes a directory and generates a CSV containing a list of files. """
    filelist = create_filelist(args.directory)
    create_csv_from_list(filelist, 'filelist.csv')



if __name__ == '__main__':
    CLI_ARGS = parse_arguments()
    main(CLI_ARGS)
