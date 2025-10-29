import sys

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

def parse_huffman_code(i: int, sources_count: int):
    print_msg(f"Enter Huff_{i} ", end="")
    print_msg(f"(eg. [11,0,10]): ", "cyan", end="")
    code = [i.strip() for i in input().strip('[]\n ').split(',')]
    if len(code) != sources_count:
        print_msg(f"> Error: |S| does not equal number of sources in Huff_{i}. ({sources_count} != {len(code)})", "red")
        sys.exit(1)
    else:
        print_msg(f"> Huff_{i} parsed as: {code}", "gray")
        print_msg(f"> ", "gray", end="")
        for idx,v in enumerate(code, 1):
            print_msg(f"c{idx} = {v}", "gray", end=", ")
        print("\n")
        return code

# -------------------- Main --------------------
mode = input("Do you want to encode or decode? (e/d): ").strip().lower()[0]
if mode not in ("d", "e"):
    print_msg("> Error: Invalid mode. Choose 'e' or 'd'.", "red")
    sys.exit(1)

sources_count = int(input("\nEnter number of sources: "))
__set_msg = ",".join(f"s{i}" for i in range(1, sources_count + 1))
print_msg(f"> S = {{ {__set_msg} }}\n", "gray")

# Parse Huffman codes
print_msg(f"Enter Huff_E ", end="")
print_msg(f"(eg. [11,0,10]): ", "cyan", end="")
huff_e = [i.strip() for i in input().strip('[]\n ').split(',')]
if len(huff_e) != sources_count:
    print_msg(f"> Error: |S| does not equal number of sources in Huff_E. ({sources_count} != {len(huff_e)})", "red")
    sys.exit(1)
else:
    print_msg(f"> Huff_E parsed as: {huff_e}", "gray")
    for i,v in enumerate(huff_e, 1):
        print_msg(f"> c{i} = {v}", "gray")
    print("")

huffman_codes = {"h_e": huff_e}
for i in range(1, sources_count + 1):
    huffman_codes[f"h_{i}"] = parse_huffman_code(i, sources_count)

# -------------------- Encode --------------------
if mode == "e":
    print_msg(f"Enter the message to encode: ", end="")
    print_msg(f"eg. s1s2s3", "cyan")
    to_encode = [int(i) for i in input().strip().split("s") if i]

    if max(to_encode) > sources_count:
        print_msg(f"> Error: Found s{max(to_encode)} which is not in S", "red")
        sys.exit(1)

    print_msg("\nEncoded Result:", "green")
    prev_huff_i = "h_e"
    for code in to_encode:
        print(huffman_codes[prev_huff_i][code - 1], end="")
        prev_huff_i = f"h_{code}"
    print("\n")

# -------------------- Decode --------------------
else:
    print_msg("Enter the code to decode ", end="")
    print_msg("(eg. 11010):", "cyan")
    to_decode = input().strip()

    decoded = []
    prev_huff_i = "h_e"
    i = 0
    while i < len(to_decode):
        # Find the symbol that matches a prefix
        for idx, codeword in enumerate(huffman_codes[prev_huff_i], 1):
            if to_decode.startswith(codeword, i):
                decoded.append(f"s{idx}")
                prev_huff_i = f"h_{idx}"
                i += len(codeword)
                break
        else:
            print_msg(f"> Error: no matching codeword at position {i}", "red")
            sys.exit(1)

    print_msg("\nDecoded Result:", "green")
    print("".join(decoded))
