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
- `heights.py` — TreeSwift script: print `label,height` (height = max distance to any leaf)

---

## Usage

```bash
# https://morgannprice.github.io/fasttree/
FastTree -gtr -nt alignment.fa > tree_fasttree.nw

# https://iqtree.github.io/
# v2 uses --prefix ; v1.x uses -pre
iqtree2 -s alignment.phy -m GTR+I+R4 --prefix iqtree_out
# iqtree  -s alignment.phy -m GTR+I+R4 -pre iqtree_out

# https://github.com/amkozlov/raxml-ng
raxml-ng --msa alignment.phy --model GTR+I+R4 --prefix rax_out

# https://gensoft.pasteur.fr/docs/newick-utils/1.6/nwutils_tutorial.pdf
# https://github.com/tjunier/newick_utils
nw_distance -n -s f -m p tree_fasttree.nw

# TreeSwift heights (label,height)
python heights.py tree_fasttree.nw
