import itertools
import fractions
import math

def get_probability(numerators, denominator):
    numerator_product = 1
    for numerator in numerators:
        numerator_product *= numerator

    denominator_product = denominator ** len(numerators)

    frac = fractions.Fraction(numerator=numerator_product, denominator=denominator_product)

    return frac

def get_length(probability, radix):
    return math.ceil(-math.log(probability, radix))


print('Enter your radix:')
radix = int(input())

print('Enter your extension:')
extension = int(input())

print('Enter number of sources:')
num_sources = int(input())

print("Enter denominator:")
denominator = int(input())

print("Enter numerators (separated by commas):")
numerators = [int(i) for i in input().split(",")]

print("Sort by? (p for probabilities/l for lengths):")
sort_choice = input()

print()
# ==============
num_codewords = num_sources**extension

idx = 1
codewords = []
probabilities = []
lengths = []
for combo in itertools.product(range(1, num_sources +  1), repeat=extension):
    codeword = "".join(f"s{i}" for i in combo)
    prob = get_probability([numerators[j - 1] for j in combo], denominator)
    length = get_length(prob, radix)

    codewords.append(codeword)
    probabilities.append(prob)
    lengths.append(length)

    idx += 1

data = list(zip(codewords, probabilities, lengths))
if sort_choice == "p":
    data.sort(key=lambda x: x[1])
elif sort_choice == "l":
    data.sort(key=lambda x: x[2])

print(f"{'Idx':>3}  {'Codeword':<10}  {'Probability':>10}  {'Length':>10}")
for i, data_entry in enumerate(data):
    print(f"{i + 1} {data_entry[0]:>10} {data_entry[1]:>10} {data_entry[2]:>10}")

