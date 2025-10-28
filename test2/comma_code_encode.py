import re

def gen_comma_codes(length: int) -> list[str]:
    codes: list[str] = []
    for i in range(length + 1):
        code: str = ''
        for _ in range(i):
            code += '1'

        if i != length:
            code += '0'

        codes.append(code)

    return codes


def comma_code_encode(comma_code: list[str], symbols: list[str]) -> str:
    encoded_message: str = ''
    for si in symbols:
        i: int = int(si[-1])
        encoded_message += comma_code[i - 1]

    return encoded_message


print('Enter the comma code length:')
length: int = int(input())
comma_code: list[str] = gen_comma_codes(length)

print('Enter the message:')
message: str = input()
symbols: list[str] = re.findall(r's\d', message)

encoded_message = comma_code_encode(comma_code, symbols)

print(f'Encoded message: {encoded_message}')
