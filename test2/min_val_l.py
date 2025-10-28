import re

def kraft_mcmillan_total(radix: int, lengths: list[int]) -> float:
    total: float = 0
    for length in lengths:
        total += 1/(radix)**length
    return total

def find_l(radix: int, lengths: list[int]) -> int:
    for i in range(1000):
        lengths.append(i)
        total: float = kraft_mcmillan_total(radix, lengths)
        lengths.pop()
        if total <= 1:
            return i
        i += 1
    return -1

print('Enter radix:')
radix: int = int(input())

print('Enter lengths:')
lengths = [int(i) for i in re.findall(r'\d', input())]

print(f'Minimum ℓ: {find_l(radix, lengths)}')
