import sys
from typing import List, Dict, Iterable, Tuple

def outcome_probability_given_hidden_path(
    symbols: list[str], #possible emitted symbols (alphabet)
    symbol_string: list[str], #emitted string
    states: list[str], #possible hidden states
    state_path: list[str], #hidden path π
    emission: dict[str, dict[str, float]], #emission matrix (probability of emitting each symbol from each state)
) -> float:
    """
    Find the conditional probability Pr(x|π) that x will be emitted given that the HMM follows the hidden path π.
    """

    probability = 1.0 #finally probability is product of emission probabilities

    for i in range(len(symbol_string)): #loop through each position i in our emitted string
        hidden = state_path[i] #hidden state at position i
        symbol = symbol_string[i] #symbol at position i
        probability *= emission[hidden][symbol] #given hidden, we look up the emission probability of the symbol and multiply it with current

    return probability #return total probability
