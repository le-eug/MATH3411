import re
import math

def generate_codes(lengths, radix=2):
    codes = []
    current = [0] * max(lengths)  # track digits for each position
    
    for l in lengths:
        # build code string from first l digits
        code = ''.join(str(d) for d in current[:l])
        codes.append(code)
        
        # increment code in the given radix
        i = l - 1
        while i >= 0:
            current[i] += 1
            if current[i] < radix:  # no carry needed
                break
            current[i] = 0  # reset and carry over
            i -= 1
        
        # prepare next digit if needed
        if i < 0 and l < len(current):
            current[l] = 0

    return codes

print('Enter probabilities (copy and paste entire line):')
prob_input = input()

probs = [float(i) for i in re.findall(r"\d+\.\d+", prob_input)]

print('Enter radix:')
radix = int(input())

print('Enter encoded message:')
encoded_msg = input()

lengths = [math.ceil(-math.log2(p)) for p in probs]

for i, code in enumerate(generate_codes(lengths, radix)):
    print(f"s{i + 1}: {code}")
