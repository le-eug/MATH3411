import math
import re

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


print('Enter radix:')
radix = int(input())

print('Enter probabilities (copy and paste entire line):')
prob_input = input()

probs = [float(i) for i in re.findall(r"\d+\.\d+", prob_input)]

lengths = []
for prob in probs:
    lengths.append(math.ceil(-math.log(prob, radix)))

print('Enter message:')
msg = input()

symbols = re.findall(r"s\d", msg)

codes = generate_codes(lengths, radix)

# Encode message
encoded_msg = ""
for symbol in symbols:
    # assuming a symbol is s1, s2, ..., s9
    idx = int(symbol[-1])
    
    encoded_msg += codes[idx - 1]

print("Encoded message:")
print(encoded_msg)
