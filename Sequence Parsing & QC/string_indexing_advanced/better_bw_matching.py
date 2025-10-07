import sys
from typing import List, Dict, Iterable, Tuple

def preprocess_bwt(bwt: str) -> Tuple[Dict[str, int], Dict[str, List[int]], Dict[Tuple[str, int], int]]:
    """
    Use code from previous problems to compute FirstOccurrence, Count array, and Last to First 
    (three dictionaries: character to first occurrence, character to count array (i.e. how many times each character appears up to index i in bwt), and (char, occurrence) tuple based on last column to its index in first column). 
    """
    length = len(bwt)
    firstCol = sorted(bwt) 

    firstColOccurrence = {}
    count = {char: [0] * (length + 1) for char in set(bwt)} #track count of each character in the last column
    lastColOccurrence = {}

    firstColIndex = []
    lastColIndex = []

    for i, char in enumerate(bwt): 
        occurrence = lastColOccurrence.get(char, 0)
        lastColIndex.append((char, occurrence))
        lastColOccurrence[char] = occurrence + 1

    for i, char in enumerate(firstCol):
        if char not in firstColOccurrence:
            firstColOccurrence[char] = i
        firstColOccurrence[(char, lastColOccurrence[char] - 1)] = i

        
    #compute count array    
    for i in range(length):
        char = bwt[i]
        for key in count:
            count[key][i + 1] = count[key][i] + (1 if key == char else 0)

    return firstColOccurrence, count, firstColIndex

def better_bw_matching(bwt: str, patterns: List[str]) -> List[int]:
    """
    Perform an optimized Burrows-Wheeler Matching for a set of patterns against the Burrows-Wheeler Transform of a text.
    """
    firstColOccurrence, count, firstColIndex = preprocess_bwt(bwt) #preprocess bwt using the helper function above
    matches = []

    for pattern in patterns:
        top = 0
        bottom = len(bwt) - 1

        while top <= bottom and pattern:
            char = pattern[-1] #take last character of pattern
            pattern = pattern[:-1] #remove last character

            if char in firstColOccurrence: #update top and bottom based on FirstOccurrence and Count
                top = firstColOccurrence[char] + count[char][top]
                bottom = firstColOccurrence[char] + count[char][bottom + 1] - 1
            else:
                matches.append(0) #value of 0 if pattern not found
                break
        else:
            matches.append(bottom - top + 1) #total number of matches for that pattern added
    
    return matches
