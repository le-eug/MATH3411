#prime factorization
def factor(n):
    f = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        f[n] = 1
    return f

# Euler's totient right here
def phi(n):
    f = factor(n)
    result = n
    for p in f:
        result *= (1 - 1/p)
    return int(result)

def is_primitive_root(g, n):
    ph = phi(n)
    fac = factor(ph)

    if gcd(g, n) != 1:
        return False

    for q in fac:
        if pow(g, ph // q, n) == 1:
            return False
    return True

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n = int(input("Given should be Z_n. Enter n:"))
primitive_roots = [g for g in range(1, n) if is_primitive_root(g, n)]
primitive_roots = list(filter(lambda g: g != n, primitive_roots))
print("Primitive roots modulo", n, ":", primitive_roots)
