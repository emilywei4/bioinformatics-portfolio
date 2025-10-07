import sys
from typing import List, Dict, Iterable, Tuple

def most_likely_path(
    symbols: list[str],
    symbol_string: str,
    states: list[str],
    transition: dict[str, dict[str, float]],
    emission: dict[str, dict[str, float]],
) -> str:
    """
    Find a path that maximizes the (unconditional) probability Pr(x, π) over all possible paths π.
    """
    
    length = len(symbol_string) #length of emitted string
    numStates = len(states) #total number of states

    viterbiGraph = [{} for _ in range(length)] #initialize viterbi graph (determines max prob for each state at position i)
    backtrack = [{} for _ in range(length)] #initialize backtrack, which stores backtracking info to reconstruct the hidden path

    startProb = 1 / numStates #initial state has equal probability

    for state in states: #initialize first column
        viterbiGraph[0][state] = startProb * emission[state][symbol_string[0]]
        backtrack[0][state] = None #no previous state to mark in backtrack

    for i in range(1, length): #fill in viterbi graph
        for stateCurr in states: #compute the max probability path to each current state
            maxProb = -1.0
            maxPrevState = None

            for statePrev in states: #loop through every possible previous state and update maxProb and maxPrevState to the highest probability
                probability = viterbiGraph[i - 1][statePrev] * transition[statePrev][stateCurr] * emission[stateCurr][symbol_string[i]]
                if probability > maxProb:
                    maxProb = probability
                    maxPrevState = statePrev
                    
            viterbiGraph[i][stateCurr] = maxProb 
            backtrack[i][stateCurr] = maxPrevState

    maxProbability = -1.0
    endState = None
    for s in states: #loop through each state and compare the probability stored in the last column of the viterbi graph and choose state with highest probability
        if viterbiGraph[length - 1][s] > maxProbability:
            maxProbability = viterbiGraph[length - 1][s]
            endState = s

    optimalPath = [endState]
    for i in range(length - 1, 0, -1): #reconstruct path backwards
        optimalPath.append(backtrack[i][optimalPath[-1]])

    return "".join(reversed(optimalPath)) #reverse backward path to get forward path
