import sys

def profile_most_probable_kmer(text: str, k: int,
                               profile: list[dict[str, float]]) -> str:
    """Identifies the most probable k-mer according to a given profile matrix.

    The profile matrix is represented as a list of columns, where the i-th element is a map
    whose keys are strings ("A", "C", "G", and "T") and whose values represent the probability
    associated with this symbol in the i-th column of the profile matrix.
    """
    compareProbability = -1
    mostProbKmer = ''

    for i in range(len(text) - k + 1):
        kmer = text[i:i + k]
        probability = 1
        
        for j in range(k):
            nucleotide = kmer[j]
            
            probability *= profile[j][nucleotide]
        
        if probability > compareProbability:
            compareProbability = probability
            mostProbKmer = kmer

    return mostProbKmer
