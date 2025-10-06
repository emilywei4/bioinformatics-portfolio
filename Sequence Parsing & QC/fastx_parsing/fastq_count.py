#!/usr/bin/env python3
import sys, gzip

# Usage: python fastq_count.py <reads.fastq.gz>

file = gzip.open(sys.argv[1], "rt")
lines = file.read().splitlines()
file.close()

count = 0
for line in lines:
    if line.startswith("+"):   # use '+' instead of '@' to avoid false matches
        count += 1

print(count)
