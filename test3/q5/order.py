import math

def ord(a, m):
    if math.gcd(a, m) != 1:
        return None

    i = 1
    while True:
        if a ** i % m == 1:
            return i
        i += 1


print("Enter your modulus:")
m = int(input())

print("Enter the number you are finding the order of:")
a = int(input())

print("Order:")
print(ord(a,m))
