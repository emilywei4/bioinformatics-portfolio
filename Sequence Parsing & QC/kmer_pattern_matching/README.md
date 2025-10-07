# K-mer Pattern Matching

**Problem**  
How can we identify the most frequent k-mers in a DNA sequence while allowing for sequencing errors or mutations (up to *d* mismatches)?

**Approach**  
These Python scripts implement basic string algorithms used in genomic data analysis.  
They generate all possible *d*-mismatch neighbors of a k-mer, compute Hamming distances, and count approximate k-mer occurrences across a DNA string to find common sequence motifs.

---

## Files
- **neighbors.py** — Generates all neighbors of a sequence within a given Hamming distance.  
- **frequent_kmers_mismatches.py** — Finds the most frequent k-mers with up to *d* mismatches.  
- **Helper:** `HammingDistance(string1, string2)` — Counts base mismatches between two equal-length strings.

---

## Usage

```bash
# Import the neighbor function
from neighbors import neighbors

neighbors("ACG", 1)
# → ['CCG', 'GCG', 'TCG', 'AAG', 'AGG', 'ATG', 'ACA', 'ACC', 'ACT', 'ACG']

# Find the most frequent 4-mers with ≤1 mismatch
from frequent_kmers_mismatches import frequent_words_with_mismatches

text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
frequent_words_with_mismatches(text, 4, 1)
# → ['GCAT', 'CATG']
