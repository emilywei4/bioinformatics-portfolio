#!/usr/bin/env python3
import sys, treeswift

# Read trees
mut_tree = treeswift.read_tree_newick(sys.argv[1])
tim_tree = treeswift.read_tree_newick(sys.argv[2])

# Distance from a node to the root (sum of edge lengths on the path up)
def dist_to_root(node):
    d = 0.0
    while node != node.tree.root:
        e = node.get_edge_length()
        d += e
        node = node.get_parent()
    return d

# Build label -> TTR dictionaries using leaves only
mut_leaves = mut_tree.label_to_node('leaves')
tim_leaves = tim_tree.label_to_node('leaves')

mut_ttr = {}
for label, node in mut_leaves.items():
    mut_ttr[label] = dist_to_root(node)

tim_ttr = {}
for label, node in tim_leaves.items():
    tim_ttr[label] = dist_to_root(node)

# For shared labels, print ratio = mutation_TTR / time_TTR
for label in sorted(set(mut_ttr.keys()) & set(tim_ttr.keys())):
    ratio = mut_ttr[label] / tim_ttr[label]
    print(label + "," + ("%.6f" % ratio))
