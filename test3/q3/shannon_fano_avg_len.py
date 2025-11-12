import math

print("Enter radix:")
radix = int(input())

print("Enter denominator:")
denominator = int(input())

print("Enter numerators:")
numerators = [int(i) for i in input().split(",")]

probabilities = [i / denominator for i in numerators]
lengths = [-math.log(prob, radix) for prob in probabilities]

avg_len = sum(prob * length for prob, length in zip(probabilities, lengths))

print("Average codeword length:")
print(f"{avg_len:.3f}")
