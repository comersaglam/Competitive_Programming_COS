import numpy as np

n = int(1e5)
n= 1
S0 = n//3
S1 = (n+2) // 3
S2 = (n+1) // 3

p0 = np.float64(S0 / n)
p1 = np.float64(S1 / n)
p2 = np.float64(S2 / n)

transition_matrix = np.array([[0, 0, 0], 
                                [p2, p0, p1], 
                                [p1, p2, p0]])
pi = np.array([p0,p1,p2])

def markov_step(state, transition_matrix):
    return np.dot(state, transition_matrix)

#k = int(input())
k = 10000
expected = 0
for i in range(1, k+1):
    x = pi[0]
    expected += (i)*pi[0]
    pi = markov_step(pi, transition_matrix)

# 6 decimal places
print("{:.6f}".format(expected))