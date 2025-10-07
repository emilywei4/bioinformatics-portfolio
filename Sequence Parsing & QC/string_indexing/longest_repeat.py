import sys
from typing import List, Dict, Iterable, Tuple

def longest_repeat(text: str) -> str:
    """
    Find the longest repeated substring in the given text.

    For each starting index i, we compare with text. 
    At that index, we find matching substrings and continually update the longest one. 
    """
    length = len(text)
    longest = ""

    for i in range(length): #move starting position downward
        for j in range(i + 1, length): #for each starting position we compare substring starting at i to every other substring starting at j
            prefix = 0
            while j + prefix < length and i + prefix < length and text[i + prefix] == text[j + prefix]: #use a while loop to count how many characters match
                prefix += 1
                if prefix > len(longest): #if we have found a longer match then...
                    longest = text[i:i + prefix] #it becomes our return variable
    return longest #return the longest matched sequence
