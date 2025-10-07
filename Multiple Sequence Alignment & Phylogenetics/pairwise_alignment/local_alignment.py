import sys
from typing import List, Dict, Tuple

# local alignment is best used when looking for regions of similarity between two sequences that, in other areas, might be very different (i.e. conserved domains in protein sequences)
def local_alignment(match_reward: int, mismatch_penalty: int, indel_penalty: int, s: str, t: str) -> Tuple[int, str, str]:
    """
    Compute the local alignment of two strings based on match reward, mismatch penalty, and indel penalty.
    """
    n = len(s) #number of rows in the alignment graph
    m = len(t) #number of columns in the alignment graph
    maxScore = 0 #keep track of the score of the best local alignment between the two substrings
    maxI = 0
    maxJ = 0 #stores the coordinates where the max score is found (position where the best local alignment ends in our graph)

    alignmentGraph = [[0] * (m + 1) for _ in range(n + 1)] #initialize alignment graph
    backtrack = [[0] * (m + 1) for _ in range(n + 1)] #initialize backtrack for LCSOutput function

    #fill in our alignmentGraph, and from there, build our backtrack graph, so we have a path that we can follow when we build our alignments
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i - 1] == t[j - 1]: #if the characters match
                diagonalScore = alignmentGraph[i - 1][j - 1] + match_reward #characters match, so we increment the score
            else: #if characters don't match (specifically a mismatch)
                diagonalScore = alignmentGraph[i - 1][j - 1] - mismatch_penalty
            upScore = alignmentGraph[i - 1][j] - indel_penalty #deletion
            leftScore = alignmentGraph[i][j - 1] - indel_penalty #insertion

            alignmentGraph[i][j] = max(0, diagonalScore, upScore, leftScore) #for local alignment, we reset the score to 0 if it's negative

            #set up backtrack based on scores
            if alignmentGraph[i][j] == diagonalScore:
                backtrack[i][j] = 0
            elif alignmentGraph[i][j] == upScore:
                backtrack[i][j] = 1
            elif alignmentGraph[i][j] == leftScore:
                backtrack[i][j] = 2

            if alignmentGraph[i][j] > maxScore:
                maxScore = alignmentGraph[i][j]
                maxI, maxJ = i, j
        
    #using the path in backtrack, we reconstruct the alignment sequences

    alignedS = [] #initialize aligned string s that we want to return
    alignedT = [] #initialize aligned string t that we want to return 
    i, j = maxI, maxJ #this marks the end of the best local alignment, and then we backtrack
    while i > 0 and j > 0 and alignmentGraph[i][j] > 0: #continue until there are no characters in s (i = 0) left, or none in t (j = 0)
        if backtrack[i][j] == 0: #characters match
            alignedS.append(s[i - 1]) #include current s character
            alignedT.append(t[j - 1]) #include current t character
            i -= 1 #increment down since we include s
            j -= 1 #increment down since we include t
        elif backtrack[i][j] == 1: #include s but not t (deletion)
            alignedS.append(s[i - 1]) #include current s character
            alignedT.append("-") #add a gap for current t position
            i -= 1 #increment i down
        elif backtrack[i][j] == 2: #include t but not s (insertion)
            alignedS.append("-") #add a gap for current s position
            alignedT.append(t[j - 1]) #include current t character
            j -= 1 #increment j down
    
    alignedS = ''.join(reversed(alignedS)) #reverse list and join characters plus gaps into a string
    alignedT = ''.join(reversed(alignedT)) #reverse list and join character plus gaps into a string

    return maxScore, alignedS, alignedT #return a tuple of the alignment score, and aligned versions of both strings
