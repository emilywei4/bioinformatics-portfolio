#!/usr/bin/env python3
import sys
mode = sys.argv[1]
seq1 = sys.argv[2]
seq2 = sys.argv[3]

count = 0
for i in range(len(seq1)):
    if seq1[i] != seq2[i]:
        count += 1

if mode == "count":
    print(count)
elif mode == "proportion":
    print(count / len(seq1))
