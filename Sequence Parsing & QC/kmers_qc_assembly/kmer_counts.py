#!/usr/bin/env python3
import sys

# Usage: python kmer_counts.py <k> <sequence.txt>

k = int(sys.argv[1])

file = open(sys.argv[2], "r")
sequence = file.read().replace("\n", "").replace(" ", "")
file.close()

kmers = {}

for i in range(len(sequence) - k + 1):
    kmer = sequence[i:i+k]
    if kmer not in kmers:
        kmers[kmer] = 1
    else:
        kmers[kmer] += 1

for kmer in sorted(kmers.keys()):
    print(kmer + "," + str(kmers[kmer]))
