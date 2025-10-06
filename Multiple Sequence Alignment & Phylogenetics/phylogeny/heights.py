#!/usr/bin/env python3
# Usage: python heights.py tree.nw
import sys, treeswift

tree = treeswift.read_tree_newick(sys.argv[1])

def node_height(node):
    if node.is_leaf():
        return 0.0
    k = node.num_children()
    if k == 1:
        # get the only child and follow the chain
        for child in node.children:
            return child.get_edge_length() + node_height(child)
    # k >= 2: take the max over children
    best = 0.0
    for child in node.children:
        h = child.get_edge_length() + node_height(child)
        if h > best:
            best = h
    return best

for n in tree.traverse_preorder():
    label = n.get_label()
    if label:
        print(label + "," + ("%.6f" % node_height(n)))
