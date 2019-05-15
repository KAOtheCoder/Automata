from DeterministicFiniteAutomata import DeterministicFiniteAutomata
from NonDeterministicFiniteAutomata import NonDeterministicFiniteAutomata
from NonDeterministicPushDownAutomata import NonDeterministicPushDownAutomata

# A deterministic finite automata that accept only binary numbers that are multipliers of 3
# diagram source: https://en.wikipedia.org/wiki/Deterministic_finite_automaton
dfa = DeterministicFiniteAutomata(True)
dfa.addTransition("s0", 0, "s0")
dfa.addTransition("s0", 1, "s1")
dfa.addTransition("s1", 0, "s2")
dfa.addTransition("s2", 1, "s2")
dfa.addTransition("s2", 0, "s1")
dfa.addTransition("s1", 1, "s0")
dfa.setStateAccepting("s0")
dfa.setStartState("s0")
dfa.run([1,1,0])
print(dfa.computationHistory.toString())

# A nondeterministic finite machine that accept only binary numbers that have a "0" in the second to the last position.
nfa = NonDeterministicFiniteAutomata(True)
nfa.addTransition("a", 0, "a")
nfa.addTransition("a", 1, "a")
nfa.addTransition("a", 0, "b")
nfa.addTransition("b", 0, "c")
nfa.addTransition("b", 1, "c")
nfa.setStateAccepting("c")
nfa.setStartState("a")
nfa.run([1,0,1,1,0,0])
print(nfa.computationHistory.toString())

# A push down automata for L = { 0^n 1^n | n>=0 }
# diagram source: https://www.tutorialspoint.com/automata_theory/pushdown_automata_acceptance.htm
pda = NonDeterministicPushDownAutomata(True)
pda.addTransition("q1", None, None, "$", "q2")
pda.addTransition("q2", 0, None, 0, "q2")
pda.addTransition("q2", 1, 0, None, "q3")
pda.addTransition("q3", 1, 0, None, "q3")
pda.addTransition("q3", None, "$", None, "q4")
pda.setStateAccepting("q1")
pda.setStateAccepting("q4")
pda.setStartState("q1")
print(pda.run([0,0,1,1]))
print(pda.computationHistory.toString())