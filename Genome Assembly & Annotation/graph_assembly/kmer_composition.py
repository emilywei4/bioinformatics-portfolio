
import sys
from typing import List, Dict, Iterable

def kmer_composition(text: str, k: int) -> Iterable[str]:
    """Forms the k-mer composition of a string."""
    kmers = []

    for i in range(len(text) - k + 1):
        kmer = text[i:i+k]
        kmers.append(kmer)
    
    return kmers
