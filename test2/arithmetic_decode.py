import re


class Interval:
    start = 0
    end = 0

    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end


print('Enter number of symbols (including stop):')
num_symbols: int = int(input())

symbols: list[str] = []
for i in range(num_symbols):
    print(f'Enter symbol {i + 1}: ')
    symbol = input()
    symbols.append(symbol)

stop_symbol: str = symbols[-1]

print('Enter intervals: (copy and paste whole line from Q)')

# converts input into an array of Intervals
intervals = [Interval(float(i), float(j)) for i, j in re.findall(r'\[(\d*\.?\d+),(\d*\.?\d+)\)', input())]
# print([(i.start, i.end) for i in intervals]) 

print('Enter encoded message: ')
encoded_message = float(input())

curr_symbol = ''
decoded_message = ''
low = 0.0
high = 1.0
while curr_symbol != stop_symbol:
    for i, symbol in enumerate(symbols):
        interval_start = low + (high - low) * intervals[i].start
        interval_end = low + (high - low) * intervals[i].end

        if interval_start <= encoded_message < interval_end:
            decoded_message += symbol
            curr_symbol = symbol
            low = interval_start
            high = interval_end
            break

print(f'Decoded message: {decoded_message}')
