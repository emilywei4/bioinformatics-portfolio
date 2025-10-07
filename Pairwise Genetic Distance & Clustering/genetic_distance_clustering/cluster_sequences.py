#!/usr/bin/env python3
import sys, csv

csv_file = sys.argv[1]
threshold = float(sys.argv[2])

clusters = []
unique_clusters = set()
all_sequences = set()

f = open(csv_file, "r")
reader = csv.reader(f)
header = next(reader)  # skip header

for line in reader:
    seq1, seq2, dist = line[0], line[1], float(line[2])
    all_sequences.update([seq1, seq2])

    if dist <= threshold:
        unique_clusters.update([seq1, seq2])
        matching = [c for c in clusters if seq1 in c or seq2 in c]
        if not matching:
            clusters.append(set([seq1, seq2]))
        else:
            merged = set([seq1, seq2])
            for c in matching:
                merged |= c
                clusters.remove(c)
            clusters.append(merged)

f.close()

unclustered = all_sequences - unique_clusters

for c in clusters:
    print(",".join(sorted(c)))

for u in sorted(unclustered):
    print(u)
