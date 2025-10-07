# Genetic Distance & Clustering

**Problem**  
How can we compute pairwise nucleotide distances between sequences, use the TN93 model to generate substitution distances, and cluster related sequences based on a distance threshold?

**Approach**  
This workflow combines:
- a simple Python script to count or proportion mismatches between two sequences,
- the **TN93** tool for pairwise model-based distances,
- and a Python clustering script to group sequences below a given distance threshold.

---

## Files
- **Pipeline drivers (documented commands below)**  
  - TN93 — compute Tamura–Nei 93 pairwise genetic distances  
- `pairwise_distance.py` — compute raw count or proportion of mismatches between two sequences  
- `cluster_sequences.py` — group sequences by distance threshold from TN93 output  

---

## Usage

```bash
# ---------------------------
# pairwise_distance.py
# Usage: python pairwise_distance.py <mode> <seq1> <seq2>
# <mode> = "count" or "proportion"

python pairwise_distance.py count ATGCGT ATCCGT
# Output: 1

python pairwise_distance.py proportion ATGCGT ATCCGT
# Output: 0.1667

# ---------------------------
# TN93
# https://github.com/veg/tn93
# Compute pairwise Tamura–Nei 93 distances
# -o : output file
# -t : threshold (optional)
# -l : report overlap
# FASTA : input sequence file

tn93 -o distances.csv -t 1.0 -l input.fasta

# Convert CSV → space-delimited TXT using tr
cat distances.csv | tr ',' ' ' > distances.txt

# ---------------------------
# cluster_sequences.py
# Usage: python cluster_sequences.py <tn93_output.csv> <threshold>

python cluster_sequences.py distances.csv 0.015
