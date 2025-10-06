#!/usr/bin/env python3
import sys, gzip

# Usage: python mean_readlen.py <reads.fastq.gz>
# Approach:
# - Identify lines that start with '+'
# - Backtrack one line (the sequence line)
# - Add its length to a running total; divide by count at the end

file = gzip.open(sys.argv[1], "rt")
lines = file.read().splitlines()
file.close()

seqLenTot = 0
numSeqs = 0

for i, line in enumerate(lines):
    if line.startswith("+"):
        if i > 0:  # make sure there is a previous line
            seq_line = lines[i - 1].strip().replace(" ", "")
            seqLenTot += len(seq_line)
            numSeqs += 1

if numSeqs == 0:
    print(0)
else:
    avg = seqLenTot / numSeqs
    # print with two decimals like your other scripts
    print(f"{avg:.2f}")
