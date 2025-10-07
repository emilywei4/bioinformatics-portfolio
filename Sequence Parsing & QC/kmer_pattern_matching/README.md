# K-mer Pattern Matching

**Problem**  
How can we identify the most frequent k-mers in a DNA sequence while allowing up to *d* mismatches, and quickly list all neighbors of a k-mer within Hamming distance ≤ *d*?

**Approach**  
This single Python module implements classic string algorithms for early genomic analysis:
- `neighbors(s, d)` enumerates the *d*-mismatch neighborhood of a k-mer.
- `HammingDistance(a, b)` counts mismatched bases between equal-length strings.
- `frequent_words_with_mismatches(text, k, d)` tallies approximate k-mer frequencies across a sequence and returns the top patterns.

---

## Files
- `kmer_pattern_matching.py` — contains `HammingDistance`, `neighbors`, and `frequent_words_with_mismatches`.

---

## Usage

```python
from kmer_pattern_matching import neighbors, frequent_words_with_mismatches

# 1) Neighborhood of a k-mer (≤ d mismatches)
neighbors("ACG", 1)
# Example output (order may vary):
# ['CCG', 'GCG', 'TCG', 'AAG', 'AGG', 'ATG', 'ACA', 'ACC', 'ACT', 'ACG']

# 2) Most frequent k-mers with mismatches
text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
frequent_words_with_mismatches(text, 4, 1)
# Example output:
# ['GCAT', 'CATG']
