def count_ones(bitstring: str) -> int:
    total: int = 0
    for ch in bitstring:
        if int(ch) == 1:
            total += 1
    return total


def vertical_stringify(messages: list[str]) -> list[str]:
    message_len: int = len(messages[0])
    vertical_messages: list[str] = []
    for i in range(message_len):
        vertical_string: str = ''
        for j in range(len(messages)):
            vertical_string += messages[j][i]
        vertical_messages.append(vertical_string)
        vertical_string = ''
    return vertical_messages


def find_odd(parities: list[int]) -> int:
    for i, num in enumerate(parities):
        if num % 2 == 1:
            return i
    return -1


def get_word_len(messages: list[str]) -> int:
    return len(messages[0])


def get_err_posn(horizontal_err_posn: int, vertical_err_posn: int, word_len: int) -> int:
    return horizontal_err_posn * word_len + vertical_err_posn + 1


print('Enter the message:')
message: str = input()

messages: list[str] = message.split()
vertical_messages: list[str] = vertical_stringify(messages)

horizontal_parities: list[int] = [count_ones(msg) for msg in messages]
vertical_parities: list[int] = [count_ones(msg) for msg in vertical_messages]

horizontal_err_posn: int = find_odd(horizontal_parities)
vertical_err_posn: int = find_odd(vertical_parities)

word_len: int = get_word_len(messages)
err_posn: int = get_err_posn(horizontal_err_posn, vertical_err_posn, word_len)

print(f'Error in digit: {err_posn}')
print(f'Word: {horizontal_err_posn + 1}, Digit: {vertical_err_posn + 1}')

