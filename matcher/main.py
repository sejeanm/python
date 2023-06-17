# Matcher (C) 2023 sejeanm

import argparse
import matcher

VERSION = '0.0.1'
PROGRAM_NOTE = 'Matcher (C) 2023 {}' \
               'Software for finding matching for chess round' \
               'For game format everyone-with-everyone.'.format(VERSION)


def argparse_setup():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input-file', type=str, required=True, help="Input file with matching gird")
    parser.add_argument('-o', '--output-file', type=str, required=False, help="Output file", default="new_matching.csv")
    return parser


if __name__ == '__main__':
    print(PROGRAM_NOTE)
    arg_parser = argparse_setup()
    args = arg_parser.parse_args()
    print('Input file:', args.input_file)
    print('Output file:', args.output_file)

    grid = matcher.load2(args.input_file)
    game_proposal = matcher.find_matching(grid)
    print('Game proposal for next round: {}'.format(game_proposal))
