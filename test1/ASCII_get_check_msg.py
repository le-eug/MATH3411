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


def get_check_string(vertical_messages: list[str]) -> str:
    check_msg = ''
    for msg in vertical_messages:
        if count_ones(msg) % 2 == 1:
            check_msg += '1'
        else:
            check_msg += '0'
    return check_msg


print('Enter the message:')
message: str = input()

messages: list[str] = message.split()
vertical_messages: list[str] = vertical_stringify(messages)

check_string: str = get_check_string(vertical_messages)

print(f'The check string is: {check_string}')
