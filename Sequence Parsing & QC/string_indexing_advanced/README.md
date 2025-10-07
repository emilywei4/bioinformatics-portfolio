# Advanced String Indexing (BWT/FM Index)

**Problem**  
How can we invert the Burrows–Wheeler Transform (BWT) and perform fast pattern matching using FM-index style primitives?

**Approach**  
This folder focuses on BWT-based workflows:
- `inverse_burrows_wheeler_transform.py` — reconstruct the original text from its BWT.
- `better_bw_matching.py` — optimized BWT matching using FirstOccurrence + Count arrays (backward search).
- `multiple_pattern_matching.py` — build SA → BWT, then do backward search to report all start positions.

---

## Files & Key Functions

- `inverse_burrows_wheeler_transform.py`
  - `inverse_burrows_wheeler_transform(transform: str) -> str`

- `better_bw_matching.py`
  - `preprocess_bwt(bwt: str) -> tuple[dict[str,int], dict[str, list[int]], dict]`
  - `better_bw_matching(bwt: str, patterns: list[str]) -> list[int]`

- `multiple_pattern_matching.py`
  - `find_suffix_array(text: str) -> list[int]`
  - `find_bwt(text: str, suffix_array: list[int]) -> str`
  - `preprocess_bwt(bwt: str) -> tuple[dict[str,int], list[dict[str,int]]]`
  - `multiple_pattern_matching(text: str, patterns: list[str]) -> dict[str, list[int]]`

---

## Usage

```python
# 1) Inverse BWT
from inverse_burrows_wheeler_transform import inverse_burrows_wheeler_transform
original = inverse_burrows_wheeler_transform("smnpbnnaaaaa$a")

# 2) FM-style matching (counts of matches per pattern)
from better_bw_matching import better_bw_matching
counts = better_bw_matching("annb$aa", ["ana", "n"])

# 3) Multiple pattern matching (positions via SA + BWT)
from multiple_pattern_matching import multiple_pattern_matching
hits = multiple_pattern_matching("panamabananas$", ["ana", "nana", "ban"])
