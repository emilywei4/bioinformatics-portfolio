# Genome Rearrangements & Breakpoint Graphs

**Problem**  
How can we analyze genome permutations, quantify “distance” via breakpoints/two-break distance, and detect shared sequence anchors via k-mers?

**Approach**  
These small, independent scripts cover classic comparative-genomics primitives:
- `greedy_sorting.py` — sort a signed permutation using greedy reversals (records each intermediate permutation).
- `breakpoint_count.py` — count breakpoints in a signed permutation (with 0 and n+1 sentinels).
- `two_break_distance.py` — build a breakpoint graph for two genomes and compute the two-break distance using cycle counts.
- `shared_kmers.py` — find shared k-mers (including reverse complements) between two strings.

---

## Files & Key Functions

- `greedy_sorting.py`
  - `greedy_sorting(P: List[int]) -> List[List[int]]`
- `breakpoint_count.py`
  - `breakpoint_count(P: List[int]) -> int`
- `two_break_distance.py`
  - `gene_to_edge(gene: int) -> Tuple[int,int>`
  - `chromosome_to_nodes(chromosome: List[int]) -> List[int]`
  - `adjacency_edges(chromosome: List[int]) -> List[Tuple[int,int]]`
  - `breakpoint_graph(P: List[List[int]], Q: List[List[int]]) -> Dict[int, List[int]]`
  - `cycle_count(graph: Dict[int, List[int]]) -> int`
  - `two_break_distance(P: List[List[int]], Q: List[List[int]]) -> int`
- `shared_kmers.py`
  - `complement_finder(kmer: str) -> str`
  - `shared_kmers(k: int, s: str, t: str) -> List[Tuple[int,int]]`

---

## Usage

```python
# Greedy sorting (signed permutation)
from greedy_sorting import greedy_sorting
steps = greedy_sorting([+3, +4, -1, +5, -2])

# Breakpoint count
from breakpoint_count import breakpoint_count
bp = breakpoint_count([+1, -3, -4, +2])

# Two-break distance
from two_break_distance import two_break_distance
P = [[+1, -2, -3, +4]]
Q = [[+1, +2, -4, +3]]
dist = two_break_distance(P, Q)

# Shared k-mers (with reverse complements)
from shared_kmers import shared_kmers
pairs = shared_kmers(3, "AAACTCATC", "TTTCAAATC")
