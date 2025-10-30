import sys
from fractions import Fraction
import heapq
from itertools import count

# used to prioritise latest insertions first in the case of a tie
counter = count()

# value = (priority_fraction, symbol)
def push(pq, tuple):
    heapq.heappush(pq, (tuple[0], next(counter), tuple[1]))

def pop(pq):
    probability, _, symbol = heapq.heappop(pq)
    return (probability, symbol)

def print_msg(msg: str, color: str = "white", end: str = "\n"):
    colors = {
        "red": "31",
        "green": "32",
        "cyan": "36",
        "white": "37",
        "gray": "90",
    }
    color_code = colors.get(color.lower(), "37")
    print(f"\033[1;{color_code}m{msg}{end}\033[0m", end="")

def parse_M_columns(sources_count: int):
    print_msg(f"\nEnter column to calculate Huffman code of ", end="")
    print_msg(f"(eg. 1/2,1/4,1/4):", "cyan")
    fractions = [i.strip() for i in input().strip().split(',')]

    M_i = []
    for i, fraction in enumerate(fractions, start=1):
        (n, d) = fraction.split('/')
        n = int(n.strip())
        d = int(d.strip())
        push(M_i, (Fraction(n, d), [f"s{i}"]))

    if len(M_i) != sources_count:
        print_msg(f"> Error: column can only have {sources_count} probabilities", "red")
        sys.exit(1)

    return M_i

# -------------------- Main --------------------
sources_count = int(input("\nEnter number of sources: "))
__set_msg = ",".join(f"s{i}" for i in range(1, sources_count + 1))
print_msg(f"> S = {{ {__set_msg} }}\n", "gray")

radix = int(input("Enter radix: "))

nodes: list[tuple[Fraction, str]] = parse_M_columns(sources_count)

# add dummies
while radix != 2 and len(nodes) % (radix - 1) != 1:
    push(nodes, (Fraction(0, 1), "_"))

huffman_codes = {f"s{i}": "" for i in range(1, sources_count + 1)}
while True:
    to_merge: list[tuple[Fraction, str]] = [pop(nodes) for _ in range(0, radix)]
 
    merged_value = Fraction(0, 1)
    merged_symbols = []
    for i, (fraction, symbols) in enumerate(reversed(to_merge)):
        merged_value += fraction
        for symbol in symbols:
            merged_symbols.append(symbol)
            huffman_codes[symbol] = str(i) + huffman_codes[symbol]

    push(nodes, (merged_value, merged_symbols))

    if merged_value == Fraction(1, 1):
        break


print_msg(f'\nHuffman codes:', "green")
for key, value in huffman_codes.items():
    print(f"{key}: {value}")
print(f"\n[{','.join(huffman_codes.values())}]")