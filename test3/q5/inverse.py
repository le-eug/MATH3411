import math

def get_inverse(a, m):
    if math.gcd(a, m) != 1:
        return None

    return pow(a, -1, m) # thanks python!


print("Enter your modulus: ")
m = int(input())

print("Enter the number finding the inverse for: ")
a = int(input())

print("Inverse:")
print(get_inverse(a, m))
