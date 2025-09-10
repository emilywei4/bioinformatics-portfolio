#!/usr/bin/env python3
import sys

# Usage: python unique_kmers.py <k> <sequence.txt>

k = int(sys.argv[1])

file = open(sys.argv[2], "r")
sequence = file.read().replace("\n", "").replace(" ", "")
file.close()

kmers = []
for i in range(len(sequence) - k + 1):
    kmer = sequence[i:i+k]
    if kmer not in kmers:
        kmers.append(kmer)

kmers.sort()

for kmer in kmers:
    print(kmer)
