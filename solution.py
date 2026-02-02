# Students :
# Haoues Doua Hiba (Security Group 2)
# Mokhtari Anis Yassinne (AI Group 2)


# Read the NFA
def read_nfa():
    states = {'q0', 'q1', 'q2'}
    alphabet = {'a', 'b'}

    transitions = {
        ('q0', 'ε'): {'q1'},
        ('q1', 'a'): {'q1'},
        ('q1', 'b'): {'q2'},
        ('q2', 'ε'): {'q0'}
    }

    start = 'q0'
    finals = {'q2'}

    return states, alphabet, transitions, start, finals


# ε-closure
def epsilon_closure(state, transitions):
    stack = [state]
    closure = {state}

    while stack:
        s = stack.pop()
        for nxt in transitions.get((s, 'ε'), set()):
            if nxt not in closure:
                closure.add(nxt)
                stack.append(nxt)

    return closure

# Computation the new transitions
def compute_new_transitions(states, alphabet, transitions):
    closures = {s: epsilon_closure(s, transitions) for s in states}
    new_trans = {}

    for q in states:
        for a in alphabet:
            reach = set()
            for s in closures[q]:
                reach |= transitions.get((s, a), set())

            final_reach = set()
            for r in reach:
                final_reach |= closures[r]

            if final_reach:
                new_trans[(q, a)] = final_reach

    return new_trans, closures


# Compute the new finals
def compute_new_finals(states, closures, old_finals):
    return {s for s in states if closures[s] & old_finals}


# NFA with the ε
def display_nfa_with_epsilon(states, alphabet, transitions, start, finals):
    print("===== NFA WITH EPSILON =====")
    print("States:", states)
    print("Alphabet:", alphabet, "+ ε")
    print("Start state:", start)
    print("Final states:", finals)
    print("\nTransitions:")
    for (s, a), d in transitions.items():
        print(f"{s} --{a}--> {d}")


# the NFA WITHOUT the ε
def display_nfa_without_epsilon(states, alphabet, transitions, start, finals):
    print("\n===== NFA WITHOUT EPSILON =====")
    print("States:", states)
    print("Alphabet:", alphabet)
    print("Start state:", start)
    print("Final states:", finals)
    print("\nTransitions:")
    for (s, a), d in transitions.items():
        print(f"{s} --{a}--> {d}")


# ================= MAIN =================
if __name__ == "__main__":
    states, alphabet, transitions, start, finals = read_nfa()

    # Display WITH epsilon
    display_nfa_with_epsilon(states, alphabet, transitions, start, finals)

    # Remove epsilon transitions
    new_transitions, closures = compute_new_transitions(
        states, alphabet, transitions
    )
    new_finals = compute_new_finals(states, closures, finals)

    # Display WITHOUT epsilon
    display_nfa_without_epsilon(
        states, alphabet, new_transitions, start, new_finals
    )
