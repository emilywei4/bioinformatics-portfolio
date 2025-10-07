import sys
from typing import List, Dict, Iterable, Tuple

def breakpoint_count(P: List[int]) -> int:
    """
    Calculates the number of breakpoints in the given permutation.
    """
    P = [0] + P + [len(P) + 1] #add 0 and length of permutation plus 1 to the start and end because we need to check if 1 is at the start and len(P) is at the end

    breakpointCount = 0
    for i in range(len(P) - 1):
        if P[i + 1] - P[i] != 1: #if positive adjacent elements are not consecutive OR if negative adjacent elements are not reversly consecutive
            breakpointCount += 1 #increment number of breakpoints
    
    return breakpointCount
