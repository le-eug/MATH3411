def filter_lengths(input: str) -> list[int]:
    filtered: list[int] = []
    for item in input.split(','):
        # remove all non alphanumeric characters
        filtered_item: str = ''
        for ch in item:
            if ch.isnumeric():
                filtered_item += ch
        filtered.append(int(filtered_item))
    return filtered

print('Enter radix: ')
radix: int = int(input())

print('Enter lengths: ')
lengths: list[int] = filter_lengths(input())

codes: list[int] = [0] * len(lengths)

for i in range(len(lengths)):
    if i == 0:
        continue
    codes[i] = (codes[i - 1] + 1) * radix ** (lengths[i] - lengths[i - 1])

answer: str = bin(codes[len(lengths) - 1])
print(f'c{len(lengths)}: {answer[2::]}')
