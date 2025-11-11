import re
from math import log

def read_frac(input):
    frac = [float(i) for i in re.findall(r"\d+", input)]
    return frac[0]/frac[1]

markov = [[], []]
print("Enter M_1,1")
markov[0].append(float(input()))

print("Enter M_1,2")
markov[0].append(float(input()))

print("Enter M_2,1")
markov[1].append(float(input()))

print("Enter M_2,2")
markov[1].append(float(input()))

equilibrium = []
print("Enter P_1")
equilibrium.append(read_frac(input()))

print("Enter P_2")
equilibrium.append(read_frac(input()))

# Lecture 18-19 Slide 14
hm = 0
for i in range(2):
    intermediate = 0
    for j in range(2):
        intermediate += equilibrium[j] * markov[i][j] * log(markov[i][j], 2)
    hm += -intermediate

print()
print("Markov Entropy:")
print(f"{hm:.2f}")

