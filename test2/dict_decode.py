import re

print('Enter encoded dictionary: ')
message: str = input()

# Convert dictionary to list of tuples
tuples = re.findall(r'\((\w+),(\w+)\)', message)
tuples = [(int(i), item) for i, item in tuples]

dictionary = {
    0: '',
}

# Create dictionary from tuples
for i, (index, entry) in enumerate(tuples):
    dictionary[i + 1] = dictionary[index] + entry

msg: str = ''
for item in dictionary:
    msg += dictionary[item]

print(f'Message: {msg}')
