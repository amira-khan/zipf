"""
Count the occurrences of all words in a text
and write them to a CSV-file.
"""

import argparse
import string
from collections import Counter

import utilities as util


def count_words(reader):
    """Count the occurrence of each word in a string."""
    text = reader.read()
    chunks = text.split()
    stripped = [word.strip(string.punctuation) for word in chunks]
    word_list = [word.lower() for word in stripped if word]
    word_counts = Counter(word_list)
    return word_counts


def parse_command_line():
    """Parse the command line for input arguments."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('infile', type=argparse.FileType('r'),
                        nargs='?', default='-',
                        help='Input file name')
    parser.add_argument('-n', '--num',
                        type=int, default=None,
                        help='Output only n most frequent words')
    args = parser.parse_args()
    return args


def main():
    """Run the command line program."""
    args = parse_command_line()
    word_counts = count_words(args.infile)
    util.collection_to_csv(word_counts, num=args.num)


if __name__ == '__main__':
    main()
