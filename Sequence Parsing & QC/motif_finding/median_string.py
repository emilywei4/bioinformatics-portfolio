import sys

def hamming_distance(string1: str, string2: str) -> int:
    hamDist = 0
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            hamDist += 1
    return hamDist

def find_all_kmers(k: int) -> list[str]:
    kmerList = []
    nucleotides = 'ACGT'

    for i in range(4 ** k):
        kmer = ''
        temp = i
        for j in range(k):
            kmer = nucleotides[temp % 4] + kmer
            temp //= 4
        kmerList.append(kmer)

    return kmerList

def median_string(dna: list[str], k: int) -> str:
    """Identifies the median string of length k in a collection of longer strings."""
    smallestDistance = float('inf')
    medianString = ""
    kmers = find_all_kmers(k)

    for kmer in kmers:
        distance = 0
        for line in dna:
            smallestHamDist = float('inf')
            for i in range(len(line) - k + 1):
                subseq = line[i:i + k]
                hamDist = hamming_distance(kmer, subseq)
                if hamDist < smallestHamDist:
                    smallestHamDist = hamDist
            distance += smallestHamDist
        
        if distance < smallestDistance:
            smallestDistance = distance
            medianString = kmer
    
    return medianString
