print('Enter radix:')
radix: int = int(input())

print('Enter denominator:')
denominator: int = int(input())

print('Enter numerators:')
numerators_string: str = input()

numerators = [int(i) for i in numerators_string.split(',')]
probabilities = [i for i in numerators]

probabilities.sort()
merged: list[float] = []

while True:
    to_merge: list[float] = probabilities[:radix]
    leftover: list[float] = probabilities[radix:]

    merged_value = sum(to_merge)
    merged.append(merged_value)
    if merged_value >= denominator:
        break

    probabilities = [merged_value] + leftover
    probabilities.sort()

print(f'Average length: {sum(merged)}/{denominator}')
