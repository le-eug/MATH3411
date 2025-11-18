import math

print("Enter your N:")
n = int(input())

print("How many choices do you have? (exclude None of these if its a choice):")
num_choices = int(input())

a_choices = []
print("Enter your choices:")
for _ in range(num_choices):
    a_choices.append(int(input()))

for a in a_choices:
    if math.gcd(a, n) != 1:
        continue

    if pow(a, n - 1, n) != 1:
        continue

    print()
    print("Answer:")
    print(a)
    exit()

print("None of these")

