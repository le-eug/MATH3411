def filter_isbn(isbn: str) -> str:
    filtered_isbn: str = ''
    for ch in isbn:
        if ch == 'x' or ch == 'X':
            filtered_isbn += ch
        elif ch.isnumeric():
            filtered_isbn += ch
    return filtered_isbn


def calculate_isbn_trial_sum(isbn: str, err_posn: int, trial_digit: int) -> int:
    total: int = 0
    for i, ch in enumerate(isbn):
        if i == err_posn - 1:
            total += (i + 1) * trial_digit
        else:
            if ch == 'X' or ch == 'x':
                total += (i + 1) * 10
            else:
                total += (i + 1) * int(ch)
    return total


def correct_error_digit(isbn: str, err_posn: int) -> int:
    correct_isbn_digit = -1
    for trial_digit in range(11):
        if calculate_isbn_trial_sum(isbn, err_posn, trial_digit) % 11 == 0:
            correct_isbn_digit = trial_digit
    return correct_isbn_digit


print('Enter your ISBN:')
isbn: str = input()
isbn = filter_isbn(isbn);

print('Enter error position:')
err_posn: str = input()

correct_digit: int = correct_error_digit(isbn, int(err_posn));

if correct_digit == -1:
    print('No error found.')
elif correct_digit == 10:
    print('Correct digit: X')
else:
    print(f'Correct digit: {correct_digit}')
