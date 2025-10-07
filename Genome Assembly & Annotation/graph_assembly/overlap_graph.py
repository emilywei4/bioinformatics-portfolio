import sys
from typing import List, Dict, Iterable

def overlap_graph(patterns: List[str]) -> Dict[str, List[str]]:
    """Forms the overlap graph of a collection of patterns."""

    #sort lexicographically
    patterns.sort()

    #initialize dictionary to return
    overlaps = {}

    #start with first kmer and compare to subsequent ones to find a pair with overlap
    for kmer1 in range(len(patterns)):
        for kmer2 in range(len(patterns)):

            #take the prefix of the first and the suffix of the second and compare
            if kmer1 != kmer2 or patterns[kmer1] == patterns[kmer2]:
                suffixKmer1 = patterns[kmer1][1:] #suffix defined as last k-1 letters
                prefixKmer2 = patterns[kmer2][:-1] #prefix defined as first k-1 letters

                #if the prefix of the first one matches the suffix of the second then they overlap
                if suffixKmer1 == prefixKmer2:
                    if patterns[kmer1] not in overlaps:
                        overlaps[patterns[kmer1]] = []
                    #add kmer2 as a value for the kmer1 key in dictionary overlaps if it's not already there
                    if patterns[kmer2] not in overlaps[patterns[kmer1]]:
                        overlaps[patterns[kmer1]].append(patterns[kmer2])

    return overlaps
