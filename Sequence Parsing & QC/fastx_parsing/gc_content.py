#!/usr/bin/env python3
import sys

# Usage: python gc_content.py <input.fasta>

file = open(sys.argv[1], "r")
lines = file.read().splitlines()
file.close()

i = 0
while i < len(lines):
    line = lines[i].strip()
    if line.startswith(">"):
        # header (sequence identifier)
        header = line[1:].strip()

        # move to the first sequence line
        i += 1
        sequence_parts = []

        # collect all sequence lines until the next header or file end
        while i < len(lines) and not lines[i].startswith(">"):
            # remove spaces per correction note
            sequence_parts.append(lines[i].replace(" ", "").strip())
            i += 1

        sequence = "".join(sequence_parts)
        totalBP = len(sequence)

        # count C/G bases (case-insensitive)
        cgBP = 0
        for base in sequence:
            if base == "C" or base == "c" or base == "G" or base == "g":
                cgBP += 1

        # avoid zero-division if an empty record appears
        if totalBP == 0:
            cgPercent = 0.0
        else:
            cgPercent = (cgBP / totalBP) * 100.0

        # print: header,GC%
        print(f"{header},{cgPercent:.2f}")

        # don't i += 1 here; the while already advanced i to the next header/file end
        continue
    else:
        # non-header line before first header; skip
        i += 1
