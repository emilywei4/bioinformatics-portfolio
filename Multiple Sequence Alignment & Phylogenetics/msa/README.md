# Multiple Sequence Alignment & Pairwise Scoring

**Problem**  
How can we align multiple sequences—both de novo and reference-guided—and compute pairwise similarity scores to evaluate sequence relationships?

**Approach**  
This workflow uses **MAFFT** for de novo multiple sequence alignment and **ViralMSA** for reference-guided viral genome alignment.  
A simple Python script (`pairwise_alignment.py`) demonstrates how to compute alignment scores between all sequence pairs, building intuition for how sequence similarity is quantified.

---

## Files
- **MAFFT** — de novo multiple sequence alignment  
- **ViralMSA** — reference-guided alignment for viral genomes  
- `pairwise_alignment.py` — compute pairwise alignment scores for all sequences in a FASTA file  

---

## Usage

```bash
# https://mafft.cbrc.jp/alignment/server/index.html
# Perform de novo multiple sequence alignment
mafft --retree 2 input.fa > output.aln

# https://github.com/niemasd/ViralMSA
# Reference-guided multiple sequence alignment
# Required arguments:
#   -s : input sequences (FASTA)
#   -r : reference genome (FASTA)
#   -e : email
#   -o : output directory
ViralMSA.py -s sequences.fa -r ref.fa -e you@email.com -o viralmsa_out

# Custom pairwise scoring script
# Compute alignment similarity across all pairs
python pairwise_alignment.py input.fa
