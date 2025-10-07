import sys
from typing import List, Dict, Iterable, Tuple

def inverse_burrows_wheeler_transform(transform: str) -> str:
    """
    Generate the inverse of the Burrows-Wheeler Transform.
    """
    length = len(transform)

    firstCol = sorted(transform) #first column is our BWT compression sorted lexicographically

    firstColOccurrence = {}
    lastColOccurrence = {}

    firstColIndex = []
    lastColIndex = []

    #track occurrences of each character in the last column
    for char in transform: #last column is just our BWT
        occurrence = lastColOccurrence.get(char, 0)
        lastColIndex.append((char, occurrence))
        lastColOccurrence[char] = occurrence + 1

    #track occurrences of each character in the first column
    for char in firstCol:
        occurrence = firstColOccurrence.get(char, 0)
        firstColIndex.append((char, occurrence))
        firstColOccurrence[char] = occurrence + 1

    #map location of corresponding value in first column for each value in last column
    lastFirst = {firstColIndex[i]: i for i in range(length)}

    original = [] #reconstruct original string
    index = transform.index('$') #start at row that has $ in the first column

    for _ in range(length):
        char, occurrence = lastColIndex[index] #extract character and its occurrencee
        original.append(char) #add character to our result
        index = lastFirst[(char, occurrence)] #move to corresponding index of character in last column to first column

    return "".join(original[::-1]) #reverse string and return
