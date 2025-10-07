import sys
from typing import List, Dict, Iterable

# g[u] is the list of neighbors of the vertex u
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
    if nodeCurr == None:
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
