import math

print("Enter your n:")
n = int(input())

t = 0
s = 0
for curr_t in range(math.ceil(math.sqrt(n)), n + 1):
    curr_s_square = curr_t**2 - n
    curr_s = math.sqrt(curr_s_square)

    # s is a square
    if int(curr_s) == curr_s:
        t = curr_t
        s = curr_s
        break

a = t - s
b = t + s

print(f"b - a:")
print(int(b - a))
