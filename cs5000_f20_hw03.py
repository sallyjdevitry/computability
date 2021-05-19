###############################################
# cs5000_f20_hw03.py
# Sally Devitry
# A01980316
###############################################
from itertools import chain

def display_dfa(dfa):
    print("STATES: ", dfa[0])
    print("SIGMA: ", dfa[1])
    print("START STATE: ", dfa[3])
    print("DELTA:")
    i = 0
    for key in dfa[2]:
        print(str(i) + ") d" + str(key) + "), = " + str(dfa[2][key]))
        i += 1
    print("FINAL STATES: " + str(dfa[4]))


def nfa_to_dfa(nfa):
    myQueue = [tuple([nfa[3]])]
    visited = set()
    DFA_DELTA = {}
    while len(myQueue) != 0:
        state = myQueue.pop()
        visited.add(state)
        for transition in nfa[1]:
            next = getAllReachableFromState(state, transition, nfa[2])
            DFA_DELTA[(state, transition)] = next
            if (next not in visited):
                myQueue.append(next)

    startStateNFA = nfa[3]
    finalStatesNFA = nfa[4]
    finalStatesDFA = []
    for state in DFA_DELTA:
        for fState in finalStatesNFA:
            if fState in state[0]:
                if state[0] not in finalStatesDFA:
                    finalStatesDFA.append(state[0])

    DFA = (visited, nfa[1], DFA_DELTA, tuple([startStateNFA]), finalStatesDFA)
    return DFA

def getAllReachableFromState(currStates, transition, nfaDelta):
    reachableStatesSet = []
    for state in currStates:
        tupleToSearchFor = tuple([state, transition])
        if tupleToSearchFor in nfaDelta:
            setToAdd = nfaDelta[tupleToSearchFor]
            reachableStatesSet.append(setToAdd)
    return tuple(sorted(tuple(set(chain.from_iterable(reachableStatesSet)))))
