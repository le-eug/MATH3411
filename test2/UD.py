import re

def uniquely_decodable(codewords: list[str]):
    # Start with differences between pairs of codewords
    def suffix_diff(w1, w2):
        if w2.startswith(w1):
            return w2[len(w1):]
        elif w1.startswith(w2):
            return w1[len(w2):]
        return None

    # Build initial set of suffixes
    D = set()
    for x in codewords:
        for y in codewords:
            s = suffix_diff(x, y)
            if s:
                D.add(s)
    seen = set(D)

    while D:
        new_D = set()
        for d in D:
            for c in codewords:
                if d.startswith(c):
                    new_D.add(d[len(c):])
                if c.startswith(d):
                    new_D.add(c[len(d):])
        if "" in new_D:
            return False  # Empty string means ambiguity
        new_D -= seen
        seen |= new_D
        D = new_D
    return True


print('Enter the codes: ')
codewords = re.findall(r'c\d+\s*=\s*([01?]+)', input())
codewords = [codeword for codeword in codewords if codeword.isnumeric()]

print('Enter the choices:')
choices: list[str] = []
for i in range(4):
    choices.append(input())

for choice in choices:
    if uniquely_decodable(codewords + [choice]) is True:
        print(f'The answer is: {choice}')
        exit(0)

print("The answer is: None of these")
