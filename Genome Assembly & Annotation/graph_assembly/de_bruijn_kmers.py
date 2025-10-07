import sys
from typing import List, Dict, Iterable

def de_bruijn_kmers(k_mers: List[str]) -> Dict[str, List[str]]:
    """Forms the de Bruijn graph of a collection of k-mers."""
    
    k_mers.sort()
    #create our de bruijn graph that we want to return
    deBruijnGraph = {}

    #create a node for the suffix of the kmer and a node for the prefix of the kmer
    for k_mer in k_mers:
        suffix = k_mer[:-1]
        prefix = k_mer[1:]

        #if the suffix isn't in the graph, initialize a list, and then add the prefix as a connecting node
        if suffix not in deBruijnGraph:
            deBruijnGraph[suffix] = []
        deBruijnGraph[suffix].append(prefix)
    
    return deBruijnGraph
