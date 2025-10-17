import math

print('Enter your codeword: ')
codeword: str = input()

distance: int = 0
for ch in codeword:
    if int(ch) != 0:
        distance += 1

max_errors: int = math.floor((distance - 1) / 2)
print(f'distance: {distance}')
print(f'maximal errors: {max_errors}')
