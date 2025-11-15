# Source - https://stackoverflow.com/a
# Posted by Stefan, modified by community. See post "Timeline" for change history
# Retrieved 2025-11-13, License - CC BY-SA 3.0
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


print("Enter your modulus (subscript of Z):")
modulus: int = int(input())

prime_factors = get_prime_factors(modulus)
num_units = totient(modulus, prime_factors)

print("Number of units:")
print(num_units)
