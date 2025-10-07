import sys
from typing import List, Dict, Iterable, Tuple

def trie_builder(patterns: List[str]) -> Dict[str, List[str]]: #function that builds our trie (trie is built in the form of a dictionary where the keys are the nodes (letters in a pattern) and the values are the subtrees from that node)
    trie = {} #initialize root node at an empty dictionary
    for pattern in patterns: #for each pattern we get...
        node = trie #start at the root...
        for letter in pattern: #and check if each letter in pattern...
            if letter not in node: #is already a node or not
                node[letter] = {} #if it isn't we create a new node
            node = node[letter] #if it is, then we move to the child node
    return trie
  
def trie_matching(text: str, patterns: List[str]) -> Dict[str, List[int]]:
    """
    Find all starting positions in Text where a string from Patterns appears as a substring.
    """
    trie = trie_builder(patterns) #build trie
    patternPositions = {pattern: [] for pattern in patterns} #initialize our resulting dictionary (keys are patterns in text and values are lists of the indices where said pattern occurs in text)

    for i in range(len(text)): #loop through every possible starting index
        node = trie
        index = i
        patternFound = "" #initialize string that we add to as we loop/add to our return dictionary if it is found in the trie
        while True: #loop until we reach a break statement
            if len(node) == 0: #checks if there are children
                if patternFound in patternPositions: 
                    patternPositions[patternFound].append(i) #exits the loop if we found a full pattern or there are no longer matches
                break
            if index < len(text): #ensures that i is still within length of text
                letter = text[index] #if it is within text, store current index as letter
            else:
                break #if we've reached the end, we exit
            if letter in node: #if the letter we have is in the trie (i.e. in a pattern) then we add it to patternFound
                patternFound += letter
                node = node[letter] 
                index += 1 #increment i and continue moving
            else:
                break
    return patternPositions
