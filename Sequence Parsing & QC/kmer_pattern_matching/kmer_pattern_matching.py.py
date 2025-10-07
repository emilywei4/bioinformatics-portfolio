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
        return [s]
    
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

def frequent_words_with_mismatches(text: str, k: int, d: int) -> list[str]:
    """Find the most frequent k-mers with up to d mismatches in a text."""
    frequencyMap = {}
    n = len(text)

    for i in range(n - k + 1):
        pattern = text[i:i + k]
        neighborhood = neighbors(pattern, d)

        for neighbor in neighborhood:
            if neighbor not in frequencyMap:
                frequencyMap[neighbor] = 0
            frequencyMap[neighbor] += 1
    
    maxFrequency = max(frequencyMap.values())

    Patterns = []
    for pattern, freq in frequencyMap.items():
        if freq == maxFrequency:
            Patterns.append(pattern)

    return Patterns
