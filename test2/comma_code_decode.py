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


def get_symbol(comma_code: list[str], number_string: str) -> str:
    for i, codeword in enumerate(comma_code):
        if codeword == number_string:
            return f's{i + 1}'
    return ''


def comma_code_decode(comma_code: list[str], encoded_message: str) -> str:
    message: str = ''

    curr_num: str = ''
    for digit in encoded_message:
        curr_num += digit
        if digit == '0':
            message += get_symbol(comma_code, curr_num)
            curr_num = ''

    message += get_symbol(comma_code, curr_num) # could be one last symbol

    return message


print('Enter the comma code length:')
length: int = int(input())
comma_code: list[str] = gen_comma_codes(length)

print('Enter the encoded message:')
encoded_message: str = input()

print(f'Decoded message: {comma_code_decode(comma_code, encoded_message)}')
