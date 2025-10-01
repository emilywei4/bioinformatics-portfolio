# Lab 5 — Multiple Sequence Alignment (MSA)

**Goal**  
Perform multiple sequence alignments (MSA) on viral sequences using common tools and implement a simple pairwise scoring function:
- De novo alignment (MAFFT)  
- Reference-guided alignment (ViralMSA)  
- Pairwise scoring of aligned sequences (custom Python)  

**Why it matters**  
MSAs are a foundation for phylogenetics, consensus building, and comparative genomics.  
ViralMSA optimizes alignments for viral data by anchoring to a reference.  
A basic pairwise scoring exercise builds intuition for how alignments are compared.  

---

## Files
- **Pipeline drivers (documented commands below)**  
  - MAFFT (multiple sequence alignment)  
  - ViralMSA (reference-guided alignment)  
- `pairwise_alignment.py` — Compute simple alignment scores for all sequence pairs in a FASTA file.  

---

## Usage

```bash
# MAFFT
# https://mafft.cbrc.jp/alignment/server/index.html
# Perform de novo multiple sequence alignment

mafft --retree 2 input.fa > output.aln

# ViralMSA
# https://github.com/niemasd/ViralMSA
# Reference-guided MSA for viral genomes

# Required arguments:
#   -s : input sequences (FASTA)
#   -r : reference genome (FASTA)
#   -e : email
#   -o : output directory

ViralMSA.py -s sequences.fa -r ref.fa -e you@email.com -o viralmsa_out

# pairwise_alignment.py
# Lab 5, Q5 — Simple pairwise alignment scoring

python pairwise_alignment.py input.fa
