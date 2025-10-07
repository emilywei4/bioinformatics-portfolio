from typing import List, Dict

#compute in-degrees first, start with node that has an indegree of zero and continue to process
def topological_ordering(graph: dict[int, list[int]]) -> list[int]:
    #initialize a dictionary called inDegree where keys are nodes and values are the number of incoming edges
    inDegree = {}
    for nodeCurr in graph:
        if nodeCurr not in inDegree:
            inDegree[nodeCurr] = 0
        for nodeNext in graph[nodeCurr]:
            if nodeNext not in inDegree:
                inDegree[nodeNext] = 0
            inDegree[nodeNext] += 1
            
    #determine which nodes have no incoming edges
    nodes = [nodeCurr for nodeCurr in inDegree if inDegree[nodeCurr] == 0]
    #initialize our return list
    topoOrder = []

    while nodes:
        nodeCurr = nodes.pop(0)
        #add our first element with no incoming edges to topoOrder
        topoOrder.append(nodeCurr)

        #decrease the in degree of all the current nodes neighbors and once its in degree is 0, add it to the queue
        for nodeNext in graph.get(nodeCurr, []):
            inDegree[nodeNext] -= 1
            if inDegree[nodeNext] == 0:
                nodes.append(nodeNext)

    return topoOrder
