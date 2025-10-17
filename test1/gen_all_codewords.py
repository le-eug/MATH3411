from itertools import product

print('Enter the radix: ')
radix: int = int(input())

print('Enter dimension: ')
dim: int = int(input())

basis_codewords: list[str] = []
for _ in range(dim):
    print('Enter basis codeword: ')
    codeword: str = input()
    basis_codewords.append(codeword)

n = len(basis_codewords[0])
all_codewords = set()

for coeffs in product(range(radix), repeat=dim):
    result = [0] * n
    for coeff, basis in zip(coeffs, basis_codewords):
        for j in range(n):
            result[j] = (result[j] + coeff * int(basis[j])) % radix

    codeword_str = ''.join(map(str, result))
    all_codewords.add(codeword_str)

print(f'\nAll {len(all_codewords)} codewords:')
for codeword in sorted(all_codewords):
    print(codeword)
