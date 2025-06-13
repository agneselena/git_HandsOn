#!/usr/bin/env python

import sys
from argparse import ArgumentParser

parser = ArgumentParser(description='Calculate nucleotide percentage in a DNA or RNA sequence')
parser.add_argument("-s", "--seq", type=str, required=True, help="Input sequence")

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()
seq = args.seq.upper()

# Filter out invalid characters
valid_nucleotides = [nuc for nuc in seq if nuc in "ACGTU"]
if len(valid_nucleotides) != len(seq):
    print("Warning: some characters in the sequence were not recognized as nucleotides.")

length = len(valid_nucleotides)
if length == 0:
    print("No valid nucleotides found.")
    sys.exit(1)

print("Nucleotide percentages:")
for base in sorted(set(valid_nucleotides)):
    pct = 100 * valid_nucleotides.count(base) / length
    print(f"{base}: {pct:.2f}%")

