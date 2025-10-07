import sys
from typing import List, Dict, Tuple

# global alignment is when you compare two closely related sequences and want to align them entirely (i.e. two people's genomes)
def global_alignment(match_reward: int, mismatch_penalty: int, indel_penalty: int,
                     s: str, t: str) -> Tuple[int, str, str]:
    """
    Compute the global alignment of two strings based on given rewards and penalties.

    Args:
    match_reward (int): The reward for a match between two characters.
    mismatch_penalty (int): The penalty for a mismatch between two characters.
    indel_penalty (int): The penalty for an insertion or deletion.
    s (str): The first string.
    t (str): The second string.

    Returns:
    Tuple[int, str, str]: A tuple containing the alignment score and the aligned strings.
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
    
    #give top row and left column their gap penalties
    for i in range(1, n + 1): #this accounts for gaps in t (i.e. when we move down and include the character in s)
        alignmentGraph[i][0] = alignmentGraph[i - 1][0] - indel_penalty #considered a deletion (character in s and gap in t) so we subtract the penalty
        backtrack[i][0] = "↓"
    for j in range(1, m + 1): #this accounts for gaps in s (i.e. when we move right and include the character in t)
        alignmentGraph[0][j] = alignmentGraph[0][j - 1] - indel_penalty #considered an insertion (gap in s and then a character in t)
        backtrack[0][j] = "→"

    #fill in our alignmentGraph, and from there, build our backtrack graph, so we have a path that we can follow when we build our alignments
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i - 1] == t[j - 1]: #if the characters match
                diagonalScore = alignmentGraph[i - 1][j - 1] + match_reward #characters match, so we increment the score
            else: #if characters don't match (specifically a mismatch)
                diagonalScore = alignmentGraph[i - 1][j - 1] - mismatch_penalty
            upScore = alignmentGraph[i - 1][j] - indel_penalty #deletion
            leftScore = alignmentGraph[i][j - 1] - indel_penalty #insertion

            alignmentGraph[i][j] = max(diagonalScore, upScore, leftScore) 

            #set up backtrack based on scores
            if alignmentGraph[i][j] == diagonalScore:
                backtrack[i][j] = "↘"
            elif alignmentGraph[i][j] == upScore:
                backtrack[i][j] = "↓"
            elif alignmentGraph[i][j] == leftScore:
                backtrack[i][j] = "→"
        
    #using the path in backtrack, we reconstruct the alignment sequences

    alignedS = [] #initialize aligned string s that we want to return
    alignedT = [] #initialize aligned string t that we want to return 
    i, j = n, m #since we are going backward, we want to start at the end of s and t (bottom right), which is equal to alignedGraph[n][m]
    while i > 0 or j > 0: #continue until there are no characters in s (i = 0) left, or none in t (j = 0)
        if backtrack[i][j] == "↘": #characters match
            alignedS.append(s[i - 1]) #include current s character
            alignedT.append(t[j - 1]) #include current t character
            i -= 1 #increment down since we include s
            j -= 1 #increment down since we include t
        elif backtrack[i][j] == "↓": #include s but not t (deletion)
            alignedS.append(s[i - 1]) #include current s character
            alignedT.append("-") #add a gap for current t position
            i -= 1 #increment i down
        elif backtrack[i][j]: #include t but not s (insertion)
            alignedS.append("-") #add a gap for current s position
            alignedT.append(t[j - 1]) #include current t character
            j -= 1 #increment j down
    
    alignedS = ''.join(reversed(alignedS)) #reverse list and join characters plus gaps into a string
    alignedT = ''.join(reversed(alignedT)) #reverse list and join character plus gaps into a string

    return alignmentGraph[n][m], alignedS, alignedT #return a tuple of the alignment score, and aligned versions of both strings
