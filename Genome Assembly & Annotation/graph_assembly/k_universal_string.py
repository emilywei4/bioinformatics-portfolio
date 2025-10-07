import sys
from typing import List, Dict, Iterable

def binary_kmers(k: int) -> List[str]:

    binaryKmers = []

    #there are 2^k possible binary k-mers of length k and this converts each number to binary/adds leading zeroes when necessary to maintain length k
    for i in range(2**k):
        binaryKmer = bin(i)[2:].zfill(k)
        binaryKmers.append(binaryKmer)
    
    return binaryKmers

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

        for key in dbGraph:
            dbGraph[key].sort()
    
    return dbGraph

def eulerian_cycle(g: Dict[str, List[str]]) -> Iterable[str]:
    """Constructs an Eulerian cycle in a graph."""

    #create a stack for the current path (allows us to backtrack)
    currentPath = []

    #initialize eulerian cycle
    eulerianCycle = []

    #move through the graph, starting at a random node
    nodeCurr = None
    for node in g:
        #if g[node] isn't empty, meaning there are outgoing edges, start exploring (exit loop)
        if g[node]:
            nodeCurr = node
            break

    #if none of the nodes have outgoing edges anymore, then we've found our cycle
    if nodeCurr is None:
        return eulerianCycle
    
    #use a stack to start exploring our current path
    currentPath.append(nodeCurr)

    #loop continues while stack is non-empty
    while currentPath:
        node = currentPath[-1]
        #check if the node still has outgoing edges
        if g[node]:
            #move to the next node
            nodeNext = g[node].pop()
            #add next node to our current path
            currentPath.append(nodeNext)
        else:
            #check if the node has no more outgoing edges, and if so, remove it and add it to the cycle to backtrack
            eulerianCycle.append(currentPath.pop())
    
    #return path in reverse order because nodes were added from stack in reverse order to cycle (last in, first out)
    return eulerianCycle[::-1]

def k_universal_string(k: int) -> str:
    """Generates a k-universal circular string."""

    #generate a list of all possible binary kmers of length k
    kmers = binary_kmers(k)

    #construct a de bruijn graph (input are suffixes and output are prefixes via an adjacency list, like we've been doing)
    dbGraph = de_bruijn_kmers(kmers)

    #calculate the eulerian cycle based on our de bruijn graph
    eulerianCycle = eulerian_cycle(dbGraph)

    #since eulerianCycle results in a list, we need to form the path by appending the last letter of each node, starting with the complete first node
    circularString = eulerianCycle[0]
    for i in range(1, len(eulerianCycle)):
        circularString += eulerianCycle[i][-1]
    
    return circularString
