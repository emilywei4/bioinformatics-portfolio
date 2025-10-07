# Hidden Markov Models (HMMs)

**Problem**  
How do we (1) compute the probability of an observed sequence given a hidden path, and (2) infer the most likely hidden path for a sequence?

**Approach**  
Two small scripts cover the core HMM routines you’ll be asked about most often:
- `outcome_probability_given_hidden_path.py` — multiplies emission probabilities along a **known** hidden path to compute `Pr(x | π)`.
- `viterbi_most_likely_path.py` — classic **Viterbi** dynamic program to find the most likely hidden state path `π*` for an observed sequence `x`.

---

## Files & Key Functions

- `outcome_probability_given_hidden_path.py`  
  - `outcome_probability_given_hidden_path(symbols, symbol_string, states, state_path, emission) -> float`

- `viterbi_most_likely_path.py`  
  - `most_likely_path(symbols, symbol_string, states, transition, emission) -> str`

---

## Usage

```python
# 1) Probability of x given a known hidden path π
from outcome_probability_given_hidden_path import outcome_probability_given_hidden_path

symbols = ["A","B"]
states = ["H","L"]
symbol_string = list("ABABBA")
state_path = list("HHLHLL")
emission = {
    "H": {"A": 0.6, "B": 0.4},
    "L": {"A": 0.3, "B": 0.7},
}

px_given_pi = outcome_probability_given_hidden_path(
    symbols=symbols,
    symbol_string=symbol_string,
    states=states,
    state_path=state_path,
    emission=emission,
)

# 2) Viterbi: most likely hidden path π* for x
from viterbi_most_likely_path import most_likely_path

transition = {
    "H": {"H": 0.7, "L": 0.3},
    "L": {"H": 0.4, "L": 0.6},
}

pi_star = most_likely_path(
    symbols=symbols,
    symbol_string="ABABBA",
    states=states,
    transition=transition,
    emission=emission,
)
