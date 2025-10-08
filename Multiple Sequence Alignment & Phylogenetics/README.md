# Multiple Sequence Alignment & Phylogenetics

Algorithms that underlie alignment and tree building, from dynamic programming on pairs to small multi-sequence routines and hidden Markov models. The goal is to show core ideas cleanly so you can explain tradeoffs and recurrences.

## What’s inside
- **pairwise_alignment/** — LCS, longest-path on DAG, global (Needleman–Wunsch) and local (Smith–Waterman) alignment.
- **msa/** — lightweight helpers for working with multiple alignments (profiles/consensus-oriented utilities).
- **advanced_alignment_dp/** — 3-sequence MLCS (3D DP) and a topological ordering helper for DAG-based DP.
- **hidden_markov_models/** — probability of an observed string given a hidden path, and Viterbi for the most likely path.
- **phylogeny/** — small utilities oriented around tree construction/evaluation inputs and outputs.
- **temporal_phylogenetics/** — helpers for time-aware analyses (handling sequence dates / temporal metadata).

_Check the subfolder READMEs for function lists and minimal examples._
