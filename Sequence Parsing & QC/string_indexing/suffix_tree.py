import sys
from typing import List, Dict, Iterable, Tuple

def suffix_tree_builder(text: str) -> Dict[str, dict]:
    tree = {} #create the root of the suffix tree
    for i in range(len(text)): #loop through all suffixes in text
        suffix = text[i:] #start at i plus rest of the string is the suffix
        nodeCurr = tree #start at the root as we traverse

        while suffix: #continue to loop while there is a suffix
            nodeFound = False #initialize this to tell us if a matching edge was found in the current node

            for edge in list(nodeCurr.keys()): #iterate over keys in nodeCurr to see what existing substrings extend from the node
                lengthCom = 0 #count how many characters between current edge and suffix

                while lengthCom < min(len(edge), len(suffix)) and edge[lengthCom] == suffix[lengthCom]: #check if the characters match both in the edge we are at and the suffix we are at
                    lengthCom += 1 #if they match, we increment the length they have in common

                if lengthCom > 0: #if at least one character matched...
                    if lengthCom == len(edge) and lengthCom < len(suffix): #checks if entire edge is matched and the suffix keeps going
                        nodeCurr = nodeCurr[edge]
                        suffix = suffix[lengthCom:]
                        nodeFound = True
                        break
                    else: 
                        matched = edge[:lengthCom] #set variable equal to the substring that matches the beginning of the suffix
                        oldBranched = edge[lengthCom:] #set variable equal to what we have already branched off of matched
                        newBranched = suffix[lengthCom:] #set variable equal to what we have to create in our suffix tree as a branch

                    if oldBranched: #check if we already have a branch off of matched
                        subtree = nodeCurr.pop(edge)
                        nodeCurr[matched] = {oldBranched: subtree} #existing edge now needs to split off into two branches (old and new branched), so we create a key with matched and set its value to a dictionary with key oldBranched and value as subtree that was associated with edge
                    else:
                        nodeCurr[matched] = nodeCurr.pop(edge)

                    if newBranched: #check if there is remaining letters after the new common suffix
                        nodeCurr[matched][newBranched] = {} #add a new branch

                    nodeCurr = nodeCurr[matched]
                    suffix = newBranched
                    nodeFound = True
                    break
                
            if not nodeFound: #if there is no common edge, we add a new one
                nodeCurr[suffix] = {}
                break
    
    return tree #return constructed trie

def get_edges(tree: Dict) -> List[str]: #get edge labels from suffix tree
    edges = [] #initialize empty list
    for edge in sorted(tree.keys()):
        edges.append(edge) #add current edge label to edges
        edges.extend(get_edges(tree[edge])) #recursively call function on subtrees to get labels from all levels
    return edges #return edges

def suffix_tree(text: str) -> List[str]: #take in string and return list of all edge labels in tree
    """
    Construct a suffix tree from the given text.
    """
    tree = suffix_tree_builder(text) #build suffix tree
    edges = get_edges(tree) #traverse tree and append all edges to list
    return edges
