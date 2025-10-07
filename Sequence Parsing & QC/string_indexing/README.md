# String Indexing & Pattern Matching

**Problem**  
How can we efficiently find patterns in strings and build indexes that support fast search?

**Approach**  
This set implements classic text-index data structures and transforms used across bioinformatics:
- `trie_matching.py` — build a trie over patterns and scan text for all pattern occurrences.
- `suffix_tree.py` — construct a simple suffix tree and list its edge labels.
- `longest_repeat.py` — brute-force longest repeated substring (teaching/demo scale).
- `suffix_array.py` — compute suffix array by lexicographic sorting of suffixes.
- `burrows_wheeler_transform.py` — produce the BWT by sorting cyclic rotations.

---

## Files & Key Functions

- `trie_matching.py`
  - `trie_builder(patterns: List[str]) -> Dict[str, List[str]]`
  - `trie_matching(text: str, patterns: List[str]) -> Dict[str, List[int]]`

- `suffix_tree.py`
  - `suffix_tree_builder(text: str) -> Dict[str, dict]`
  - `get_edges(tree: Dict) -> List[str]`
  - `suffix_tree(text: str) -> List[str]`

- `longest_repeat.py`
  - `longest_repeat(text: str) -> str`

- `suffix_array.py`
  - `suffix_array(text: str) -> List[int]`

- `burrows_wheeler_transform.py`
  - `burrows_wheeler_transform(text: str) -> str`

---

## Usage

```python
# Trie pattern matching
from trie_matching import trie_matching
hits = trie_matching("AATCGGGTTCAATCGGGGT", ["ATCG", "GGGT"])

# Suffix tree edge labels
from suffix_tree import suffix_tree
edges = suffix_tree("ATAAATG$")

# Longest repeated substring
from longest_repeat import longest_repeat
lr = longest_repeat("ATATCGCGATAT")

# Suffix array
from suffix_array import suffix_array
sa = suffix_array("panamabananas$")

# Burrows–Wheeler transform
from burrows_wheeler_transform import burrows_wheeler_transform
bwt = burrows_wheeler_transform("panamabananas$")
