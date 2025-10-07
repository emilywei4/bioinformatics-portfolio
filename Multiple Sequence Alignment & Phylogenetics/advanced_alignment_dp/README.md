# Advanced Alignment & Graph-Based DP

**Problem**  
How can we extend sequence alignment beyond two strings and represent dependencies between tasks or subproblems using graph topologies?

**Approach**  
This section demonstrates two advanced but clear algorithmic ideas built on top of dynamic programming and graph traversal:

- `multiple_alignment.py` — computes a **3-string Multiple Longest Common Subsequence (MLCS)** alignment and backtracks to reconstruct all three aligned strings.  
- `topological_ordering.py` — implements **Kahn’s algorithm** to generate a valid topological order of a directed acyclic graph (DAG), which is essential for running DP on DAGs (e.g., longest path, scheduling, or dependency resolution).

---

## Files & Key Functions

- `multiple_alignment.py`
  - `multiple_alignment(s1, s2, s3) -> (score, aligned_s1, aligned_s2, aligned_s3)`
- `topological_ordering.py`
  - `topological_ordering(graph: dict[int, list[int]]) -> list[int]`

---

## Usage

```python
# Multiple alignment (3-way LCS)
from multiple_alignment import multiple_alignment
score, a1, a2, a3 = multiple_alignment("ATATCCG", "TCCGA", "ATGTACTG")

print(score)
print(a1)
print(a2)
print(a3)

# Topological ordering (DAG)
from topological_ordering import topological_ordering
graph = {5:[11], 7:[11,8], 3:[8,10], 11:[2,9,10], 8:[9]}
print(topological_ordering(graph))
