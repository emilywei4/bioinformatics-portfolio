import sys
from typing import List, Dict, Iterable

def de_bruijn_kmers(k_mers: List[str]) -> Dict[str, List[str]]:
    """Forms the de Bruijn graph of a collection of k-mers."""
    
    #create our de bruijn graph that we want to return
    dbGraph = {}

    #create a node for the suffix of the kmer (last k -1 characters) and a node for the prefix of the kmer (first k-1 characters)
    for k_mer in k_mers:
        suffix = k_mer[:-1]
        prefix = k_mer[1:]

        #add an edge from suffix to prefix(es) via an adjacency list
        if suffix not in dbGraph:
            dbGraph[suffix] = []
        dbGraph[suffix].append(prefix)
    
    return dbGraph

def eulerian_path(g: Dict[str, List[str]]) -> Iterable[str]:
    """Constructs an Eulerian path in a graph."""

    #because we want to start with the node that has an inDegree less than its outDegree, we need to calculate the inDegree and outDegree
    inDegree = {}
    outDegree = {}

    for key, value in g.items():
        #outDegree is the number of values (prefixes) for that key (suffix)
        outDegree[key] = len(value)
        #iterate through the connectedNodes (node that the current key is pointing to)
        for connectNode in value:
            #increment the in degree of the connectNode
            inDegree[connectNode] = inDegree.get(connectNode, 0) + 1
            #make sure that connectedNode is present in outDegree and if not, initialize
            if connectNode not in outDegree:
                outDegree[connectNode] = 0
        #check if key is in inDegree and if it has no incoming edges, it's inDegree should be set to 0
        if key not in inDegree:
            inDegree[key] = 0
    
    #initialize the start node
    startNode = list(g.keys()) [0]

    #if a node's out degree is larger than its in degree, then it should be the start node
    for node in g:
        compareOut = outDegree[node] if node in outDegree else 0
        compareIn = inDegree[node] if node in inDegree else 0
        if compareOut > compareIn:
            startNode = node
            break

    #initialize stack with start node
    currentPath = [startNode]
    eulerianPath = []

    #loop through our stack
    while currentPath:
        #we look at the last node in the stack
        node = currentPath[-1]
        #if the current node exists AND has outgoing edges, move the first outgoing edge to the next node
        if node in g and g[node]:
            currentPath.append(g[node].pop(0))
        #if there are no outgoing edges, then backtrack
        else:
            eulerianPath.append(currentPath.pop())
    
    #due to using a stack, we have to return the nodes in reverse order to get the proper path
    eulerianPath.reverse()
    return eulerianPath

def string_reconstruction(patterns: List[str], k: int) -> str:
    """Reconstructs a string from its k-mer composition."""
    
    #build our de bruijn graph
    dbGraph = de_bruijn_kmers(patterns)

    #from our debruijn graph, determine the eulerian cycle (path)
    path = eulerian_path(dbGraph)

    #start at our first kmer
    text = path[0]

    #for each subsequent kmer, we add the last character of the current kmer to our string to account for overlap 
    for i in range(1, len(path)):
        text += path[i][-1]

    return text
