import argparse
import os
import os.path

import stagger

def _parse_arguments():
    argparser = argparse.ArgumentParser(
            prog='ipodcopier',
            description='Copy music files from source to target.')
    argparser.add_argument('source', metavar='SOURCE_PATH',
            help='Path to source directory, where the iPod device is mounted.')
    argparser.add_argument('target', metavar='TARGET_PATH',
            help='Path to target directory, where the files are to be organized.')
    return argparser.parse_args()

def main():
    args = _parse_arguments()

if __name__ == '__main__':
    main()

