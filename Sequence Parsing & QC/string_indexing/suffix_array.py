import sys
from typing import List, Dict, Iterable, Tuple

def suffix_array(text: str) -> List[int]:
    """
    Generate the suffix array for the given text.
    """
    indices = list(range(len(text))) #initialize list of all starting indices
    indices.sort(key=lambda i: text[i:]) #use a lambda function that returns each suffix starting at i and sort lexicographically using python's sort function
    return indices #return suffix array
