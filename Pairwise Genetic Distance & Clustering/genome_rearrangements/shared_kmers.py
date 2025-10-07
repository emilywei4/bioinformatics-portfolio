import sys
from typing import List, Dict, Iterable, Tuple

def complement_finder(kmer: str) -> str: #find the reverse complement of an inputted kmer
    complement = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    return ''.join(complement[base] for base in reversed(kmer))

def shared_kmers(k: int, s: str, t: str) -> List[Tuple[int, int]]: #find kmers that appear in both s and t (including reverse complements)
    """
    Find all shared k-mers between two strings s and t. We account for the same or reverse complement form. 
    """
    sKmers: Dict[str, List[int]] = {} #initialize dictionary to store all kmers in s

    for i in range(len(s) - k + 1): #extract kmers from s and store their starting positions in sKmers
        kmer = s[i:i + k]
        if kmer not in sKmers:
            sKmers[kmer] = []
        sKmers[kmer].append(i)

    samePositions = []
    for j in range(len(t) - k + 1): #scan all kmers in t and see if they exist in sKmers
        tKmer = t[j:j + k]
        tReverseComp = complement_finder(tKmer) #find all reverse complement kmers in t

        if tKmer in sKmers: #if we find a match, we store that pair of kmers
            for i in sKmers[tKmer]:
                samePositions.append((i, j))
        
        if tReverseComp in sKmers: #check reverse complement matches
            for i in sKmers[tReverseComp]:
                samePositions.append((i, j))
    
    return samePositions
