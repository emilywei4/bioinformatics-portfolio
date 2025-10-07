import sys
from typing import List, Dict, Tuple

def longest_path(s: int, t: int, e: Dict[int, List[Tuple[int, int]]]) -> Tuple[int, List[int]]:
    """
    Calculate the longest path between two nodes in a weighted directed acyclic graph.

    Args:
    s (int): The starting node.
    t (int): The ending node.
    e (Dict[int, List[Tuple[int, int]]]): A dictionary representing the graph, where keys are nodes,
        and values are lists of tuples (neighbor, weight).

    Returns:
    Tuple[int, List[int]]: A tuple containing the length of the longest path and the list of nodes in the path.
    """
    
    longestDistance = {} #stores longest distance from s to each node
    backtrack = {} #show prev node for each node in the longest path (helps us reconstruct the path)

    DAGNodes = sorted(set(e.keys()).union(set(v for nextNode in e.values() for v, _ in nextNode))) #we need to process the nodes in topological order to ensure we are following the directed edges in the graph

    for DAGNode in DAGNodes: 
        longestDistance[DAGNode] = float('-inf') #set to a really small number (i.e. negative infinity) because we are looking for the max path length
        backtrack[DAGNode] = None #no prev nodes to start
    
    longestDistance[s] = 0 #source node has a distance of 0

    for DAGNode in DAGNodes: #check each node in DAGNodes (topologically ordered)
        if DAGNode not in e: #this checks if a node has no outgoing edges (skip)
            continue
        for nextNode, weight in e[DAGNode]: #traverse all outgoing edges from the current node
            if longestDistance[DAGNode] + weight > longestDistance[nextNode]: #if we find a longer path to nextNode via the previous node plus the new weight, we update it to be the longest path
                longestDistance[nextNode] = longestDistance[DAGNode] + weight
                backtrack[nextNode] = DAGNode #nextNode in backtrack will point to DAGNode because DAGNode is the previous node of nextNode 
    
    returnPath = [] #initialize a list to add nodes in the return path
    curr = t #backtrack starting at the sink
    while curr is not None: #ensures we account for all nodes
        returnPath.append(curr)
        curr = backtrack[curr]
    
    returnPath.reverse() #nodes are added in reverse order (starting from sink) so we need to reverse it back (start at source) before we return it

    return longestDistance[t], returnPath #return the legnth of the longest distance to sink t and return the path it yields
