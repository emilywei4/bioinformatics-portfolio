# Graph-Based Assembly Primitives

**Problem**  
How do we go from short k-mers to assembly graphs and then reconstruct strings or universal cycles using overlap and de Bruijn graph formulations?

**Approach**  
This folder contains small, independent scripts that implement the “graph toolbox” used in genome assembly:
- `kmer_composition.py` slices a string into all k-length substrings.
- `overlap_graph.py` builds the overlap graph where edges connect k-mers whose suffix/prefix match by k−1.
- `de_bruijn_kmers.py` builds a de Bruijn graph from k-mers.
- `eulerian_cycle.py` finds an Eulerian cycle in a directed graph.
- `string_reconstruction.py` reconstructs a string from a multiset of k-mers using de Bruijn + Eulerian path.
- `k_universal_string.py` constructs a k-universal circular binary string via de Bruijn + Eulerian cycle.

> These scripts are split by sub-project headers and can be run or imported independently.  
> Any problems marked “NOT SOLVED” in notes are omitted here to keep the repo clean.

---

## Files & Key Functions

- `kmer_composition.py`
  - `kmer_composition(text, k) -> Iterable[str]`

- `overlap_graph.py`
  - `overlap_graph(patterns: List[str]) -> Dict[str, List[str]]`

- `de_bruijn_kmers.py`
  - `de_bruijn_kmers(k_mers: List[str]) -> Dict[str, List[str]]`

- `eulerian_cycle.py`
  - `eulerian_cycle(g: Dict[str, List[str]]) -> Iterable[str]`

- `string_reconstruction.py`
  - `de_bruijn_kmers(k_mers) -> Dict[str, List[str]]` (local to this script)
  - `eulerian_path(g) -> Iterable[str]`
  - `string_reconstruction(patterns: List[str], k: int) -> str`

- `k_universal_string.py`
  - `binary_kmers(k) -> List[str]`
  - `de_bruijn_kmers(k_mers) -> Dict[str, List[str]]` (local to this script)
  - `eulerian_cycle(g) -> Iterable[str]`
  - `k_universal_string(k: int) -> str`

---

## Usage

```python
# K-mer composition
from kmer_composition import kmer_composition
kmer_composition("AAGATTCTCTA", 4)

# Overlap graph
from overlap_graph import overlap_graph
overlap_graph(["ATGCG","GCATG","CATGC","AGGCA","GGCAT"])

# De Bruijn from k-mers
from de_bruijn_kmers import de_bruijn_kmers
de_bruijn_kmers(["GAGG","CAGG","GGGG","GGGA","CAGG","AGGG","GGAG"])

# Eulerian cycle (graph must have all in-degree = out-degree)
from eulerian_cycle import eulerian_cycle
eulerian_cycle({"0":["3"],"1":["0"],"2":["1","6"],"3":["2"],"4":["2"],"5":["4"],"6":["5","8"],"7":["9"],"8":["7"],"9":["6"]})

# String reconstruction from k-mers
from string_reconstruction import string_reconstruction
string_reconstruction(["CTTA","ACCA","TACC","GGCT","GCTT","TTAC"], 4)

# k-universal binary string
from k_universal_string import k_universal_string
k_universal_string(4)
