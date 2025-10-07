# Motif Finding

**Problem**  
How can we find short DNA motifs shared across sequences and select/score candidates deterministically?

**Approach**  
This folder contains three small, independent Python scripts (separate sub-projects from the same assignment).  
Each script includes exactly the functions and helpers used for that task.

- `motif_enumeration.py` — Enumerate all k-mers that appear (within Hamming distance ≤ *d*) in **every** string.
- `median_string.py` — Brute-force all k-mers and pick the one minimizing total Hamming distance to the set.
- `profile_most_probable_kmer.py` — Pick the k-mer in a string with highest probability under a given profile.

> Stochastic methods (`randomized_motif_search`, `gibbs_sampler`) are omitted here (marked incorrect/unfinished).

---

## Files
- `motif_enumeration.py` — `HammingDistance`, `neighbors`, `motif_enumeration`
- `median_string.py` — `hamming_distance`, `find_all_kmers`, `median_string`
- `profile_most_probable_kmer.py` — `profile_most_probable_kmer` (expects a list of `k` dicts as profile columns)

---

## Usage

```python
# 1) Motif Enumeration
from motif_enumeration import motif_enumeration
dna = ["ATTTGGC", "TGCCTTA", "CGGTATC", "GAAAATT"]
motifs = motif_enumeration(dna, k=3, d=1)

# 2) Median String
from median_string import median_string
median = median_string(dna, k=3)

# 3) Profile-most Probable k-mer
from profile_most_probable_kmer import profile_most_probable_kmer
profile = [
    {"A":0.2,"C":0.4,"G":0.3,"T":0.1},
    {"A":0.4,"C":0.3,"G":0.1,"T":0.2},
    {"A":0.3,"C":0.1,"G":0.5,"T":0.1},
]
text = "ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT"
best = profile_most_probable_kmer(text, k=3, profile=profile)
