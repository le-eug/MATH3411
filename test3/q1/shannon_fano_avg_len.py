import math

print("Enter radix:")
radix: int = int(input())

print("Enter denominator:")
denominator: int = int(input())

print("Enter numerators:")
numerators_string: str = input()

numerators = [int(i) for i in numerators_string.split(",")]
probabilities = [i / denominator for i in numerators]

lengths = [math.ceil(-math.log(prob, radix)) for prob in probabilities]

avg_len = 0
for prob, length in zip(numerators, lengths):
    avg_len += prob * length

print("Average codeword length:")
print(f"{avg_len}/{denominator}")
