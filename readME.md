Eliminating ε-Transitions from an NFA
Our objective

The goal of this work is to eliminate ε (epsilon) transitions from a Non-Deterministic Finite Automaton (NFA) and produce an equivalent NFA without ε-transitions. This step is required before determinizing an NFA.

Initializing NFA
States

q0, q1, q2

Alphabet

{a, b}

Start state

q0

Final state

q2

ε-transitions

q0 —ε→ q1,
q1 —a→ q1,
q1 —b→ q2,
q2 —ε→ q0

The method used
ε-Closure

For each state, its ε-closure is computed. It represents all states reachable using only ε-transitions, including the state itself.

So the computed ε-closures are :

ε-closure(q0) = {q0, q1}
ε-closure(q1) = {q1}
ε-closure(q2) = {q2, q0, q1}

New Transitions

For each state and each input symbol:

We compute the ε-closure of the state
Then, we follow the symbol transitions from all states in the closure
After that, we compute the ε-closure of the reached states
And finally we create a new transition without ε

So in our example:

From state q0:

ε-closure(q0) = {q0, q1}

On a:
q1 —a→ q1
ε-closure(q1) = {q1}
→ (q0, a) → {q1}

On b:
q1 —b→ q2
ε-closure(q2) = {q2, q0, q1}
→ (q0, b) → {q0, q1, q2}

From state q1:

(q1, a) → {q1}
(q1, b) → {q0, q1, q2}

From state q2:

(q2, a) → {q1}
(q2, b) → {q0, q1, q2}

3. Our new final states

We find that:

ε-closure(q0) ∩ {q2} ≠ ∅ → q0 (final)
ε-closure(q1) ∩ {q2} = ∅ → q1 (not final)
ε-closure(q2) ∩ {q2} ≠ ∅ → q2 (final)

This state is considered final if its ε-closure contains at least one original final state.

By that we will end up with all ε-transitions are removed, the new NFA is equivalent to the original one and the recognized language is preserved
