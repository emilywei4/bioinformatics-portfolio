# Temporal Phylogenetics: Rooting, Dating, and TTR Ratios

**Problem**  
How can we compare **time-to-root (TTR)** distances between a mutation tree and a time tree, and then **root/date** a phylogeny using standard tools?

**Approach**  
- Compute **TTR per leaf** on two trees (mutation vs. time) and print **leaf, mutation_TTR / time_TTR**.  
- Use **LSD2** and **TreeTime** to root and date trees with provided sampling dates and sequence length.

---

## Files
- **Pipeline drivers (documented commands below)**
  - LSD2 — root/date a phylogeny with dates and outgroup
  - TreeTime — root/date with regression, dates CSV, and sequence length
- `ttr_ratio.py` — compute per-leaf TTR ratio (mutation tree TTR divided by time tree TTR)

---

## Usage

```bash
# TTR ratio (TreeSwift)
# Compute mutation_TTR / time_TTR for shared leaf labels
# Usage: python ttr_ratio.py mutation_tree.nw time_tree.nw
python ttr_ratio.py mutation.nw time.nw

# LSD2 — root and date a tree
# https://github.com/tothuhien/lsd2
# -i unrooted tree, -d dates file, -g outgroup file, -s sequence length
# Example inputs:
#   dates.tsv       # two columns: <node_label>\t<decimal_date>
#   outgroup.txt    # one or more labels (newline-separated)
./lsd2 -i unrooted.nw -d dates.tsv -g outgroup.txt -s 29903

# TreeTime — root and date a tree
# https://treetime.readthedocs.io/en/latest/ ; https://github.com/neherlab/treetime
# Required: one of --aln or --sequence-length (we use --sequence-length)
# --reroot choices: min_dev | least-squares | oldest  (default: least-squares)
treetime --tree tree_input.nw \
         --dates dates.csv \
         --sequence-length 29903 \
         --outdir treetime_out \
         --reroot least-squares
