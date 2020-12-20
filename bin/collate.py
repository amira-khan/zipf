"""
Combine multiple word count CSV-files
into a single cumulative count.
"""

import csv
import argparse
from collections import Counter
import logging

import utilities as util


ERRORS = {
    'not_csv_suffix' : '{fname}: File must end in .csv',
    }


def update_counts(reader, word_counts):
    """Update word counts with data from another reader/file."""
    for word, count in csv.reader(reader):
        word_counts[word] += int(count)


def main(args):
    """Run the command line program."""
    word_counts = Counter()
    logging.info('Processing files...')
    for fname in args.infiles:
        logging.debug(f'Reading in {fname}...')
        if fname[-4:] != '.csv':
            msg = ERRORS['not_csv_suffix'].format(fname=fname)
            raise OSError(msg)
        with open(fname, 'r') as reader:
            logging.debug('Computing word counts...')
            update_counts(reader, word_counts)
    util.collection_to_csv(word_counts, num=args.num)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('infiles', type=str, nargs='*',
                        help='Input file names')
    parser.add_argument('-n', '--num',
                        type=int, default=None,
                        help='Output only n most frequent words')
    args = parser.parse_args()
    main(args)
    