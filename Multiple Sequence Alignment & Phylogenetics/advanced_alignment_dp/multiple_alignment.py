import sys
from typing import List, Dict, Iterable, Tuple

def multiple_alignment(s1: str, s2: str, s3: str) -> Tuple[int, str, str, str]:
    """
    Compute a multiple alignment solving the Multiple Longest Common Subsequence Problem for three input strings.
    """
    lenS1 = len(s1)
    lenS2 = len(s2)
    lenS3 = len(s3)

    # initialize alignment graph (same as before, but add a third element)
    alignmentGraph = [[[0] * (lenS3 + 1) for _ in range(lenS2 + 1)] for _ in range(lenS1 + 1)]

    for i in range(1, lenS1 + 1):
        for j in range(1, lenS2 + 1):
            for k in range(1, lenS3 + 1):
                if s1[i-1] == s2[j-1] == s3[k-1]:
                    alignmentGraph[i][j][k] = alignmentGraph[i-1][j-1][k-1] + 1
                else:
                    alignmentGraph[i][j][k] = max(alignmentGraph[i-1][j][k], alignmentGraph[i][j-1][k], alignmentGraph[i][j][k-1])
    
    #start at the bottom right corner of the cube (lenS1, lenS2, lenS3)
    i = lenS1
    j = lenS2
    k = lenS3

    #initialize alignment strings
    alignS1 = ""
    alignS2 = ""
    alignS3 = ""

    #backtrack from the bottom right corner until all nodes have been visited (top left corner at (0,0,0))
    while i > 0 or j > 0 or k > 0:
        #if the current characters are all equal, they get added to their alignment string and we move toward (0,0,0) in all directions
        if i > 0 and j > 0 and k > 0 and s1[i-1] == s2[j-1] == s3[k-1]:
            alignS1 = s1[i-1] + alignS1
            alignS2 = s2[j-1] + alignS2
            alignS3 = s3[k-1] + alignS3
            i-=1
            j-=1
            k-=1
        #if our current i is equal to our previous i, then we move in the ith direction, keeping j and k the same (adding dashes in alignment string)
        elif i > 0 and alignmentGraph[i][j][k] == alignmentGraph[i - 1][j][k]:
            alignS1 = s1[i-1] + alignS1
            alignS2 = "-" + alignS2
            alignS3 = "-" + alignS3
            i-=1 #only moved in i direction
        #if our current j is equal to our previous j, then we move in the jth direction, keeping i and k the same (adding dashes in alignment string)
        elif j > 0 and alignmentGraph[i][j][k] == alignmentGraph[i][j-1][k]:
            alignS1 = "-" + alignS1
            alignS2 = s2[j-1] + alignS2
            alignS3 = "-" + alignS3
            j-=1 #only moved in j direction
        #if our current k is equal to our previous k, then we move in the kth direction, keeping i and j the same (adding dashes in alignment string)
        elif k > 0 and alignmentGraph[i][j][k] == alignmentGraph[i][j][k-1]:
            alignS1 = "-" + alignS1
            alignS2 = "-" + alignS2
            alignS3 = s3[k-1] + alignS3
            k-=1 #only moved in k direction
    
    return alignmentGraph[lenS1][lenS2][lenS3], alignS1, alignS2, alignS3
