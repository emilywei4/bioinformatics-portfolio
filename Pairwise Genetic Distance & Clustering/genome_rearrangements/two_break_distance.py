import sys
from typing import List, Dict, Iterable, Tuple

def gene_to_edge(gene: int) -> Tuple[int, int]:
    """
    Turn gene into directed edge form (tuple).
    """
    avGene = abs(gene) #absolute value of gene
    if gene > 0:
        return (2 * avGene - 1, 2 * avGene) #positive gene (tail, head) is represented as 2g-1 for tail and 2g for head
    else:
        return(2 * avGene, 2 * avGene - 1) #negative gene (tail, head) is represented as 2g for tail and 2g-1 for head (so we know when to reverse)

def chromosome_to_nodes(chromosome: List[int]) -> List[int]:
    """
    Return order of directed edges (tail and head nodes) in graph. 
    """

    nodes = []
    for gene in chromosome:
        tail, head = gene_to_edge(gene) #add gene to nodes in order
        nodes.append(tail)
        nodes.append(head)
    
    return nodes

def add_undirected(adj: Dict[int, List[int]], u: int, v: int):
    """
    Add an undirected edge from u to v.
    """
    if u not in adj:
        adj[u] = [] #if node is not already in graph, we initialize
    if v not in adj:
        adj[v] = [] #if node is not already in graph, we initialize
    #create bi-directional connection between u and v
    adj[u].append(v)
    adj[v].append(u)

def adjacency_edges(chromosome: List[int]) -> List[Tuple[int, int]]:
    """
    Gives us the adjacency edges for a chromosome in a given genome. 
    """
    nodes = chromosome_to_nodes(chromosome) #take in chromosome and convert to list of nodes
    edges = []
    length = len(nodes)
    for i in range(0, length, 2): #loop through nodes in pairs because those represent directed edges
        iHead = nodes[i + 1] #get head of gene i
        nextTail = nodes[(i + 2) % length] #get the tail of the next gene
        edges.append((iHead, nextTail)) #connect them to make genome circular
    return edges

def breakpoint_graph(P: List[List[int]], Q: List[List[int]]) -> List[Tuple[int, int]]: 
    """
    Build a breakpoint graph using both P and Q genomes.
    """

    breakpointGraph = {} #initialize adjacency graph

    for chromosome in P: #add adjacency edges from P
        for edge in adjacency_edges(chromosome): #get adjacency and then...
            add_undirected(breakpointGraph, edge[0], edge[1]) #adds bi-directional edges

    for chromosome in Q: #add adjacency edges from Q
        for edge in adjacency_edges(chromosome): #get adjacency and then...
            add_undirected(breakpointGraph, edge[0], edge[1]) #adds bi-directional edges

    return breakpointGraph

def cycle_count(graph: Dict[int, List[int]]) -> int: #returns number of cycles in breakpoint graph of P and Q
    visited = set() #keep track of visited nodes (avoid duplicate counts)
    graphCycles = 0 #initialize our number of cycles

    for node in graph: #loop through nodes in adjacency list
        if node not in visited: #if not visited, we traverse via DFS
            graphCycles += 1 #new cycle found
            stack = [node] #initialize our DFS stack

            while stack: #visit all nodes in the current cycle and mark them as visited before we move onto next cycle
                nodeCurr = stack.pop()
                visited.add(nodeCurr)

                for nodeNext in graph[nodeCurr]:
                    if nodeNext not in visited:
                        stack.append(nodeNext)
                        visited.add(nodeNext)
    
    return graphCycles

def two_break_distance(P: List[List[int]], Q: List[List[int]]) -> int:
    """
    Calculate the two-break distance between two genomes P and Q.
    """
    edges = breakpoint_graph(P, Q) #construct our breakpoint graph
    graphCycles = cycle_count(edges) #count number of cycles in graph
    syntenyBlocks = sum(len(chromosome) for chromosome in P) #number of synteny blocks is equal to the number of genes
    return syntenyBlocks - graphCycles #find two break distance by subtracting blocks from cycles
