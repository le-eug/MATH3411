import math

print("Enter probability:")
probability = float(input())

print("Enter radix:")
radix = int(input())

length = math.ceil(-math.log(probability, radix))
print("Length:")
print(length)
