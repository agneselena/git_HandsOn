#!/usr/bin/env python

import sys
import re
from argparse import ArgumentParser

# Argument parsing
parser = ArgumentParser(description='Classify a sequence as DNA or RNA and optionally search for a motif.')
parser.add_argument("-s", "--seq", type=str, required=True, help="Input sequence (DNA or RNA)")
parser.add_argument("-m", "--motif", type=str, required=False, help="Motif to search in the sequence")

# Show help if no arguments
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

# Sequence classification
args.seq = args.seq.upper()  # Convert sequence to uppercase

# Validate if the sequence contains only valid nucleotides
if re.fullmatch(r'[ACGTU]+', args.seq):
    # Check for T and U to determine type
    if 'T' in args.seq and 'U' in args.seq:
        print("Invalid sequence: contains both T and U")
    elif 'T' in args.seq:
        print("The sequence is DNA")
    elif 'U' in args.seq:
        print("The sequence is RNA")
    else:
        print("The sequence could be either DNA or RNA")
else:
    print("The sequence is not valid DNA or RNA (must contain only A, C, G, T, or U)")

# Motif search 
if args.motif:
    args.motif = args.motif.upper()
    print(f'Searching for motif "{args.motif}" in sequence...')
    if args.motif in args.seq:
        print("Motif FOUND")
    else:
        print("Motif NOT FOUND")

