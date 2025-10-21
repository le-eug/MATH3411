import re

print('Enter lengths:')
lengths = [int(i) for i in re.findall(r'\d', input())]

radix: int = 1
total: float = 0
while True:
    for length in lengths:
        total += 1 / radix ** length
    if total <= 1:
        break
    else:
        radix += 1
        total = 0

print(f'Min radix: {radix}')
