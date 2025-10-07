import sys
from typing import List, Dict, Iterable, Tuple

def find_suffix_array(text: str) -> List[int]:
    """
    Compute suffix array by sorting sorting the starting indices by the corresponding suffixes
    """
    return sorted(range(len(text)), key=lambda i: text[i:]) #return indices of starting positions of all suffixes sorted lexicographically

def find_bwt(text: str, suffix_array: List[int]) -> str:
    """
    Compute BWT using suffix array.
    """
    return ''.join(text[i - 1] if i > 0 else text[-1] for i in suffix_array) #iterates over each index in suffix_array(for i > 0, it takes character preceding suffix AND for i == 0, wraps around and takes last character)
        
def preprocess_bwt(bwt: str) -> Tuple[Dict[str, int], List[Dict[str, int]]]:
    """
    Compute: firstColOccurrence (map each character to its first occurrence in the first column) and count array(cumulative counts of each character up to that index).
    """
    length = len(bwt)
    firstCol = sorted(bwt)
    firstColOccurrence = {}
    for i, char in enumerate(firstCol):
        if char not in firstColOccurrence:
            firstColOccurrence[char] = i
    
    count = []
    curr = {}
    for i in range(length + 1):
        count.append(curr.copy()) #append copy of current count to dictionary, so we can update original and move to next
        if i < length:
            char = bwt[i]
            curr[char] = curr.get(char, 0) + 1

    return firstColOccurrence, count

def multiple_pattern_matching(text: str, patterns: List[str]) -> Dict[str, List[int]]:
    """
    Find all starting positions in text where each string from patterns appears as a substring.
    """
    suffix_array = find_suffix_array(text)
    bwt = find_bwt(text, suffix_array)

    firstColOccurrence, count = preprocess_bwt(bwt) #use helper function to get first occurrences and check points
    matches = {pattern: [] for pattern in patterns}

    for pattern in patterns: #loop over patterns and initialize top and bottom
        top = 0
        bottom = len(bwt) - 1
        original = pattern
        found = True #check if entire pattern is found (only return then)

        while top <= bottom and pattern: #while in between top adn bottom...
            #process pattern from left to right
            char = pattern[-1] #take last character of pattern
            pattern = pattern[:-1] #remove last character

            if char in firstColOccurrence: #if character occurs in BWT...
                top = firstColOccurrence[char] + count[top].get(char, 0) #set top pointer to index of char in first col PLUS cumulative count of char in BWT up to top
                bottom = firstColOccurrence[char] + count[bottom + 1].get(char, 0) - 1 #set bottom pointer to first occurrence of char plus cumulative count up to bottom + 1 to account for zero based indexing
                if top > bottom: 
                    found = False
                    break
            else:
                found = False
                break
        
        if found and pattern == "": #ensure that entire pattern was processed
            validOccurrences = [i for i in suffix_array[top: bottom + 1] if i + len(original) <= len(text)] #ensure occurrences occur where substring is long enough to be fully found
            matches[original] = sorted(validOccurrences)
        else:
            matches[original] = [] #if entire pattern not found, make empty list

    return matches
