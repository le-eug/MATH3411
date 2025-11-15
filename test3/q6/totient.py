def get_prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def totient(modulus, prime_factors):
    result = modulus
    for p in set(prime_factors):
        result *= 1 - 1 / p
    return result

print("Enter number you are taking totient of:")
x = int(input())

print("Totient:")
print(totient(x, get_prime_factors(x)))


