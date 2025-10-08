# Sequence Parsing & QC

Small, readable scripts for working with sequencing files, k-mers/motifs, and classic text indexes (suffix array/BWT/FM-style). These are the building blocks behind many downstream tasks.

## What’s inside
- **fastx_parsing/** — FASTA/FASTQ parsing and basic metrics (GC%, read counts, length stats).
- **kmer_pattern_matching/** — frequent k-mers with mismatches; neighbors/Hamming distance helpers.
- **motif_finding/** — motif enumeration, median string, profile-most-probable, randomized search and Gibbs (where implemented).
- **kmers_qc_assembly/** — k-mer-driven checks that connect parsing to assembly intuition.
- **string_indexing/** — trie, suffix tree/array, and Burrows–Wheeler transform.
- **string_indexing_advanced/** — inverse BWT and FM-style backward search for fast pattern matching.

_See subfolder READMEs for functions and quick examples._
