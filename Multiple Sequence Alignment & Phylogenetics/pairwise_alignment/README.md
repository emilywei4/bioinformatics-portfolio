# Pairwise Alignment

**Problem**  
How can we compute core pairwise alignment tasks (LCS, longest path in a DAG (for scoring), and global/local sequence alignment) using dynamic programming?

**Approach**  
These scripts implement classic DP formulations for sequence comparison:
- `longest_common_subsequence.py` builds an LCS length/backtrack grid and outputs the LCS string.
- `longest_path_dag.py` computes the longest path between two nodes in a weighted DAG (useful for scoring formulations).
- `global_alignment.py` performs Needleman–Wunsch style global alignment with match/mismatch/indel scoring.
- `local_alignment.py` performs Smith–Waterman style local alignment with score reset at 0.

> Note: An “overlap alignment” function was listed but not implemented in the original notes; it’s intentionally **omitted** to keep this folder clean and interview-ready.

---

## Files & Key Functions

- `longest_common_subsequence.py`
  - `longest_common_subsequence(s: str, t: str) -> str`

- `longest_path_dag.py`
  - `longest_path(s: int, t: int, e: Dict[int, List[Tuple[int, int]]]) -> Tuple[int, List[int]]`

- `global_alignment.py`
  - `global_alignment(match_reward: int, mismatch_penalty: int, indel_penalty: int, s: str, t: str) -> Tuple[int, str, str]`

- `local_alignment.py`
  - `local_alignment(match_reward: int, mismatch_penalty: int, indel_penalty: int, s: str, t: str) -> Tuple[int, str, str]`

---

## Usage

```python
# LCS
from longest_common_subsequence import longest_common_subsequence
longest_common_subsequence("AACCTTGG", "ACACTGTGA")

# Longest path in DAG
from longest_path_dag import longest_path
graph = {0: [(1, 5), (2, 3)], 1: [(3, 6)], 2: [(3, 4)], 3: []}
longest_path(0, 3, graph)  # -> (best_score, node_path)

# Global alignment (Needleman–Wunsch)
from global_alignment import global_alignment
score, a_s, a_t = global_alignment(
    match_reward=1, mismatch_penalty=1, indel_penalty=1,
    s="PLEASANTLY", t="MEANLY"
)

# Local alignment (Smith–Waterman)
from local_alignment import local_alignment
score, a_s, a_t = local_alignment(
    match_reward=1, mismatch_penalty=1, indel_penalty=1,
    s="MEANLY", t="PENALTY"
)
