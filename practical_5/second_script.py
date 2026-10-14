import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--file", help="CSV file to read", required=True)
args = parser.parse_args()

with open(args.file, 'r') as f:
    f.reader = csv.reader(f)
    for row in f.reader:
        print(row[0], row[1], row[2])
