import sys
from typing import List, Dict, Iterable, Tuple

def greedy_sorting(P: List[int]) -> List[List[int]]:
    """
    Perform the Greedy Sorting algorithm on a given permutation.
    """
    permutations = [] #each intermediate permutation is stored here and then returned at the end
    permutationLength = len(P) #length of inputted permutation P

    for k in range(permutationLength): #iterate over each kth position in the permutation
        if abs(P[k]) != k + 1: #check if the element is already in its correct position or not (we address signs later)
            for i in range(k, permutationLength): #search for the correct number in the remaining permutationLength - k positions
                if abs(P[i]) == k + 1: #if we find a match, then we perform a reversal
                    P[k:i+1] = [-x for x in P[k:i+1][::-1]] #we take the segment from index k to i and then reverse it and make all their signs negative
                    permutations.append(P[:]) #add the intermediate permutation to the list we end up returning
                    break #once the number is in the right position, we are done with this if statement
        if P[k] == -(k + 1): #now we check if the signs match
            P[k] = -P[k] #if they don't match, we change them
            permutations.append(P[:]) #add this permutation to the return list
        
    return permutations
