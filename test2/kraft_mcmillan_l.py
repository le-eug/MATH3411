# INSTRUCTIONS:
# Please enter the lengths separated by commas, excluding the 'ℓ'

import math

def kraft_mcmillan_total(radix: int, lengths: list[int]) -> float:
    total: float = 0
    for length in lengths:
        total += 1/(radix)**length
    return total

def find_l(radix: int, lengths: list[int], k: float) -> int:
    for length in lengths:
        k -= (1/radix)**length

    # now k is 1/radix ** something
    # that something is the l we want
    return round(math.log(k, 1/radix))

print('Enter radix:')
radix: int = int(input())

print('Enter lengths:')
init_input: str = input()
lengths = [int(item.strip()) for item in init_input.split(',')]

print('Enter K numerator:')
k_num: int = int(input())

print('Enter K denominator:')
k_den: int = int(input())

print(f'Target ℓ: {find_l(radix, lengths, k_num/k_den)}')

