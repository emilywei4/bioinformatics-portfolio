import sys
from typing import List, Dict, Iterable, Tuple

def burrows_wheeler_transform(text: str) -> str:
    """
    Generate the Burrows-Wheeler Transform of the given text.
    """
    variations = [text[i:] + text[:i] for i in range(len(text))] #create all rotation of text (starting at ending at each index)
    variations.sort() #sort lexicographically using python's sort function
    bwt = ''.join(variation[-1] for variation in variations) #combine last characters in each variation to generate bwt
    return bwt
