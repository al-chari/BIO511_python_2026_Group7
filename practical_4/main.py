#!/usr/bin/env python3
from premade_script import codons
import argparse
import os
from premade_script import exercise_function as translate
from collections import Counter

def existing_file(file_path):
    """This function checks if the provided file path exists and is a file."""
    if not os.path.isfile(file_path):
        raise argparse.ArgumentTypeError(f"'{file_path}' is not a valid file")
    return file_path


def main():
    # First we capture the input arguments from the command line
    parser = argparse.ArgumentParser(description="Split the sequences in a FASTA file into codons.")
    parser.add_argument('-s', '--sequence', type=existing_file, required=True, help='Path to the input FASTA file')
    args = parser.parse_args()
    
    # We first call the function from the script, and use the input file path as an argument
    sequence_codons = codons(args.sequence)
    
    # Here you need to check the output of the function
    for header, sequence in sequence_codons.items():
        print(f"{header} codons are: {sequence}")
        most_common_codon = Counter(sequence).most_common(1)
        most_common_codon = str(most_common_codon[0:1])
        print(f"The most common codon is {most_common_codon[3:6]}, appearing {most_common_codon[9:10]} times.\n")

        # This, as well as in the aminoacids, has the problem that when more than one object is repeated the same amount of times, it only gives you the first one to appear.
        # This can be resolved with a while loop and a bunch more lines of code.

    # Here you need to call the exercise_function from premade_script.py
    aa = translate(sequence_codons)
    print("\n")
    # And check the output of that function
    for header, aminoacids in aa.items():
        print(f"{header}: {aminoacids}")
        most_common_aa = Counter(aminoacids).most_common(1)
        most_common_aa = str(most_common_aa[0:1])
        print(f"The most common aminoacid is {most_common_aa[3:4]}, appearing {most_common_aa[7:8]} times.\n")
    print

if __name__ == "__main__":
    main()
