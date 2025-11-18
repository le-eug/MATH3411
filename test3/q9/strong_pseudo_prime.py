import math


# Source - https://stackoverflow.com/q
# Posted by yonatan goldin
# Retrieved 2025-11-18, License - CC BY-SA 4.0
def is_prime(n):
    return True if len([i for i in range(2,n) if n % i == 0]) == 0 else False

def is_strong_pseudoprime(n, a):
    if n < 2:
        return False
    if is_prime(n):
        return False

    # write n - 1 as 2^s * t with t odd
    t = n - 1
    s = 0
    while t % 2 == 0:
        t //= 2
        s += 1

    if pow(a, t, n) == 1:
        return True

    for r in range(s):
        if pow(a, t*2**r, n) == n - 1:
            return True

    return False


print("Enter your N:")
n = int(input())

print("How many choices do you have? (exclude None of these if its a choice):")
num_choices = int(input())

a_choices = []
print("Enter your choices:")
for _ in range(num_choices):
    a_choices.append(int(input()))

for a in a_choices:
    if is_strong_pseudoprime(n, a):
        print()
        print("Answer:")
        print(a)
        exit()

print("None of these")

