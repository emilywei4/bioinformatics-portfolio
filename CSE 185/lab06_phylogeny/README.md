# Lab 6 — Phylogeny & Tree Operations

**Goal**  
Infer phylogenies from MSAs using three tools and practice basic tree queries:
- FastTree, IQ-TREE, RAxML-NG (ML phylogenies)
- `nw_distance` for branch lengths from Newick
- TreeSwift script to compute node heights (max distance to any descendant leaf)

**Why it matters**  
Different ML engines/model choices can change topology/support. Comfort with Newick utilities and simple tree traversals is essential for downstream comparative analyses.

---

## Files
- **Pipeline drivers (documented commands below)**  
  - FastTree (GTR, nucleotides)  
  - IQ-TREE (GTR+I+R4, custom prefix)  
  - RAxML-NG (GTR+I+R4, ML-estimated invariant sites)  
  - newick-utils `nw_distance` (print leaf labels + incident branch length)
- `lab6_q7_heights.py` — TreeSwift script: print `label,height` (height = max distance to any leaf)

---

## Usage

```bash
# FastTree — infer ML tree from nucleotide MSA (GTR + -nt)
# https://morgannprice.github.io/fasttree/
# Lab 6, Q3

FastTree -gtr -nt alignment.fa > tree_fasttree.nw

# IQ-TREE — GTR + Invariable sites + FreeRate with 4 categories
# https://iqtree.github.io/
# Lab 6, Q4
# Model string: GTR+I+R4
# Prefix notes from docs:
#   v2: --prefix myprefix
#   v1.x: -pre myprefix

# v2 example
iqtree2 -s alignment.phy -m GTR+I+R4 --prefix iqtree_out

# v1.x example (use -pre)
iqtree -s alignment.phy -m GTR+I+R4 -pre iqtree_out

# RAxML-NG — GTR + I (ML-estimated) + R4 FreeRate
# https://github.com/amkozlov/raxml-ng
# Model string: GTR+I+R4
# Lab 6, Q5

raxml-ng --msa alignment.phy --model GTR+I+R4 --prefix rax_out

# newick-utils: nw_distance — print leaf name and its incident branch length
# Tutorial: https://gensoft.pasteur.fr/docs/newick-utils/1.6/nwutils_tutorial.pdf
# Repo:     https://github.com/tjunier/newick_utils
# Lab 6, Q6
# Options:
#   -n   : print node names
#   -s f : select all leaves (labeled or not)
#   -m p : report incident branch length

nw_distance -n -s f -m p tree_fasttree.nw
# Example output (label then length):
# B  3
# A  6

# heights.py — print label,height for each labeled node=
python lab6_q7_heights.py tree.nw
# Docs: https://niema.net/TreeSwift/
