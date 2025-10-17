print('How many codewords:')
num_codewords: int = int(input())

codewords: list[str] = []
for i in range(num_codewords - 1):
    print(f'Enter codeword {i + 1}:')
    codeword_i = input()
    codewords.append(codeword_i)


