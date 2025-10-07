
import sys

def HammingDistance(string1: str, string2: str) -> int:
    hamDist = 0
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            hamDist += 1
    return hamDist

def neighbors(s: str, d: int) -> list[str]:
    """Generate neighbors of a string within a given Hamming distance."""
    if d == 0:
        return[s]
    
    if len(s) == 1:
        return ['A', 'C', 'G', 'T']
    
    prefixSubstr = s[0]
    suffixSubstr = s[1:]

    suffixNeighbors = neighbors(suffixSubstr, d)

    neighborhood = []

    for text in suffixNeighbors:
        if HammingDistance(suffixSubstr, text) < d:
            for basePair in 'ACGT':
                neighborhood.append(basePair + text)
        else:
            neighborhood.append(prefixSubstr + text)

    return neighborhood

def motif_enumeration(dna: list[str], k: int, d: int) -> list[str]:
    """Implements the MotifEnumeration algorithm."""
    Patterns = set()

    for sequence in dna:
        for i in range(len(sequence) - k + 1):
            kmer = sequence[i:i + k]
            kmerNeighbors = neighbors(kmer, d)
            for neighbor in kmerNeighbors:
                found = True
                for seq in dna:
                    foundCurr = False
                    for i in range(len(seq) - k + 1):
                        subseq = seq[i:i + k]
                        if HammingDistance(neighbor, subseq) <= d:
                            foundCurr = True
                            break
                    
                    if not foundCurr:
                        found = False
                        break
                
                if found:
                    Patterns.add(neighbor)
    return list(Patterns)
