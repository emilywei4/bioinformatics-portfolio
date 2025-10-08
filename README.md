# Bioinformatics Portfolio

This portfolio showcases algorithmic and practical solutions from my Bioinformatics work at UC San Diego. The focus is on **clear Python implementations** of core ideas used across genomics: sequence parsing, graph-based assembly, alignment DP, HMMs, string indexing (SA/BWT/FM-style), genome rearrangements, and clustering. Each area has its own README with quick examples.

---

## Project Areas

### [Sequence Parsing & QC](./Sequence%20Parsing%20%26%20QC/)
Foundations for working with sequencing data and text indexes:
- FASTA/FASTQ parsing and basic metrics (GC%, read counts, length stats)
- k-mer utilities (neighbors, frequent k-mers with mismatches)
- Motif finding (enumeration, median string, profile-most-probable, randomized/Gibbs where implemented)
- String indexing: trie, suffix tree/array, Burrows–Wheeler transform, **inverse BWT** and FM-style pattern matching

### [Genome Assembly & Annotation](./Genome%20Assembly%20%26%20Annotation/)
Graph-based assembly building blocks:
- de Bruijn graphs, Eulerian paths/cycles
- String reconstruction from k-mers
- k-universal strings (de Bruijn cycles over binary alphabet)

### [Read Mapping & Variant Calling](./Read%20Mapping%20%26%20Variant%20Calling/)
Lightweight mapping components and a tiny consensus workflow:
- Seed-and-extend primitives (indexing ideas, seeding, extension)
- Simple viral consensus construction from mapped reads

### [Multiple Sequence Alignment & Phylogenetics](./Multiple%20Sequence%20Alignment%20%26%20Phylogenetics/)
Core dynamic programming and probabilistic models that underpin alignment and tree workflows:
- Pairwise DP (LCS, longest-path on DAG, **global** and **local** alignment)
- 3-sequence MLCS (3D DP) and DAG **topological ordering** helper
- Hidden Markov Models: `Pr(x | π)` and **Viterbi** most-likely path
- Small utilities for phylogeny and temporal analyses (see subfolders)

### [Pairwise Genetic Distance & Clustering](./Pairwise%20Genetic%20Distance%20%26%20Clustering/)
Comparative genomics and unsupervised learning:
- Genome rearrangements: greedy sorting of signed permutations, **breakpoint count**, **two-break distance** via breakpoint graphs
- k-means clustering: farthest-first seeding, squared-error distortion, Lloyd’s loop
- Distance/clustering helpers

---

## Skills Demonstrated
- **Algorithm design & data structures:** dynamic programming (2D/3D), graph traversal (Eulerian paths, DAG DP), string algorithms (trie, suffix array, BWT/FM), HMMs (Viterbi)
- **Python:** clean, standalone scripts with minimal dependencies; interview-ready explanations
- **Genomics concepts:** assembly via k-mer graphs, read mapping (seed-and-extend), motif discovery, rearrangement distance, clustering

---

## How to Explore
Each top-level folder contains focused subfolders with their own README and minimal examples.

- **Browse on GitHub**, or clone locally:
  ```bash
  git clone https://github.com/yourusername/bioinformatics-problems-portfolio.git
  cd bioinformatics-problems-portfolio
