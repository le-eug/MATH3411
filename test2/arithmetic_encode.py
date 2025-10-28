import re


print('Enter number of symbols (including stop):')
num_symbols: int = int(input())

symbols: list[str] = []
for i in range(num_symbols):
    print(f'Enter symbol {i + 1}: ')
    symbol = input()
    symbols.append(symbol)

stop_symbol: str = symbols[-1]

print('Enter probabilities: (copy and paste whole line from Q)')
probabilities = [float(i) for i in re.findall(r'\d*\.?\d', input())]

# create starts for each symbol
starts = []
for i in range(len(symbols)):
    if i == 0:
        starts.append(0)
    else:
        starts.append(probabilities[i - 1] + starts[i - 1])

print('Enter message:')
message = input()

# Encoding process
start = 0
width = 1
for symbol in message:
    idx = symbols.index(symbol)

    curr_start = starts[idx]
    curr_width = probabilities[idx]

    start += curr_start * width
    width *= curr_width

print(f'Any number in the interval: [{start}, {start + width})')
