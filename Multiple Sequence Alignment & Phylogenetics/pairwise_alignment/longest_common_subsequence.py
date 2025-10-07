import sys
from typing import List, Dict, Iterable, Tuple

sys.setrecursionlimit(10000) # This line is useful to ensure you have sufficient "recursion depth" to store the recursive calls needed for this problem.

def longest_common_subsequence(s: str, t: str) -> str:
    """
    Calculate the longest common subsequence of two strings.
    """
    n = len(s) #number of rows in the alignment graph
    m = len(t) #number of columns in the alignment graph

    alignmentGraph = [] #initialize alignment graph
    for i in range(n + 1):
        row = [] #is a list to create a grid-like graph
        for j in range(m + 1):
            row.append(0) #initialize LCS lengths
        alignmentGraph.append(row)
    
    backtrack = [] #initialize backtrack for LCSOutput function
    for i in range(n + 1):
        row = []
        for j in range(m + 1):
            row.append(None) #initialize backtracking directions
        backtrack.append(row)

    #fill in alignment graph based on if characters match/assign backtrack directions
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i - 1] == t[j - 1]: #characters match
                alignmentGraph[i][j] = alignmentGraph[i - 1][j - 1] + 1 #add one to LCS length since they have a common character
                backtrack[i][j] = "↘"
            elif alignmentGraph[i - 1][j] >= alignmentGraph[i][j - 1]: #characters at i and j don't match, and in this case we don't include s's character here in the LCS because we move past it
                alignmentGraph[i][j] = alignmentGraph[i - 1][j]
                backtrack[i][j] = "↓"
            else: #move past t's character here because we don't want to include it in the LCS
                alignmentGraph[i][j] = alignmentGraph[i][j - 1]
                backtrack[i][j] = "→"
    
    return OutputLCS(backtrack, s, n, m)

#output helper function that is based on the pseudocode provided for this problem
def OutputLCS(backtrack, v, i, j):
    if i == 0 or j == 0: #if either is an empty string, then return an empty string
        return ""
    if backtrack[i][j] == "↓": #if s[i - 1] is not in the LCS, then we skip past it and move up when we backtrack
        return OutputLCS(backtrack, v, i - 1, j)
    elif backtrack[i][j] == "→": #if t[i - 1] is not in the LCS, then we skip past it and go left when we backtrack
        return OutputLCS(backtrack, v, i, j - 1)
    else: #if the characters match, then we add it to the LCS
        return OutputLCS(backtrack, v, i - 1, j - 1) + v[i - 1]
