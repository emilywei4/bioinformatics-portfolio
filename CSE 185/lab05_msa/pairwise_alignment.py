#!/usr/bin/env python3
import sys

# Read FASTA into list of sequences
file = open(sys.argv[1], "r")
lines = file.read().splitlines()
file.close()

seqs = []
seq = ""
for line in lines:
    if line.startswith(">"):
        if seq != "":
            seqs.append(seq)
            seq = ""
    else:
        seq += line
if seq != "":
    seqs.append(seq)

# Function to score two sequences
def pairwise_score(seq1, seq2):
    score = 0
    for a, b in zip(seq1, seq2):
        if a == b:
            score += 1
        elif a == "-" or b == "-":
            score += 0
        else:
            score -= 1
    return score

# Compare all pairs
for i in range(len(seqs)):
    for j in range(i+1, len(seqs)):
        s = pairwise_score(seqs[i], seqs[j])
        print("Seq" + str(i+1) + " vs Seq" + str(j+1) + ":", s)
