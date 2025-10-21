def compress(message: str):
    idx_list: list[int] = [-1]
    prefix_list: list[str] = ['']
    prefix = ''
    curr_idx = 0

    for ch in message:
        prefix += ch
        if prefix in prefix_list:
            curr_idx = prefix_list.index(prefix)
        else:
            idx_list.append(curr_idx)
            prefix_list.append(prefix)
            prefix = ''
            curr_idx = 0

    dictionary = {}
    for i in range(len(idx_list)):
        if idx_list[i] == -1:
            dictionary[i] = ''
        else:
            dictionary[i] = (idx_list[i], prefix_list[i][-1])

    return dictionary


print('Enter your message:')
message: str = input()

print(f'Dictionary: {compress(message)}')
