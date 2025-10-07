# Phylogenetic Inference & Tree Analysis

**Problem**  
How can we infer phylogenetic relationships from multiple sequence alignments and extract meaningful information (like branch lengths and node heights) from tree structures?

**Approach**  
This workflow demonstrates the use of multiple phylogenetic inference tools—**FastTree**, **IQ-TREE**, and **RAxML-NG**—to build maximum likelihood trees, followed by tree parsing and analysis using **newick-utils** and a custom **TreeSwift** script.  
Together, these steps form the foundation for downstream comparative and evolutionary genomics analyses.

---

## Files
- **Pipeline drivers (documented commands below)**  
  - FastTree (GTR, nucleotides)  
  - IQ-TREE (GTR+I+R4, custom prefix)  
  - RAxML-NG (GTR+I+R4, ML-estimated invariant sites)  
  - newick-utils `nw_distance` (print leaf labels + incident branch length)
- `heights.py` — TreeSwift script to print `label,height` (max distance to any descendant leaf)

---

## Usage

```bash
# ---------------------------
# https://morgannprice.github.io/fasttree/
# Build a maximum-likelihood tree with GTR model for nucleotides
FastTree -gtr -nt alignment.fa > tree_fasttree.nw

# ---------------------------
# https://iqtree.github.io/
# Infer ML tree with GTR+I+R4 model
# v2 uses --prefix ; v1.x uses -pre
iqtree2 -s alignment.phy -m GTR+I+R4 --prefix iqtree_out
# iqtree -s alignment.phy -m GTR+I+R4 -pre iqtree_out

# ---------------------------
# https://github.com/amkozlov/raxml-ng
# Infer ML tree with GTR+I+R4 model, ML-estimated invariant sites
raxml-ng --msa alignment.phy --model GTR+I+R4 --prefix rax_out

# ---------------------------
# https://gensoft.pasteur.fr/docs/newick-utils/1.6/nwutils_tutorial.pdf
# https://github.com/tjunier/newick_utils
# Print leaf names and incident branch lengths
nw_distance -n -s f -m p tree_fasttree.nw

# ---------------------------
# Custom TreeSwift script
# Compute node heights (label,height)
python heights.py tree_fasttree.nw
