# 2. úkol (6. 10. 2026)
# Naprogramujte rozšířený Euklidův algoritmus 
# (tzn. algoritmus bude pro vstupní přirozená čísla a, b vracet jejich největšího společného dělitele a vypíše koeficienty splňující Bézoutovu rovnost).

from math import gcd

def expanded_euklid_alg(a, b):
    """Returns the greatest common devider and numbers x and y used to satify the eqution a * x + b * y == gcd(a, b)."""
    if b == 0:
        return a, 1, 0

    if a == 0:
        return b, 0, 1
    
    a0 = a
    b0 = b

    i = 0
    x = [1, 0]
    y = [0, 1]

    while b > 0:
        q = a // b
        r = a % b

        x.append(x[i] - q * x[i + 1])
        y.append(y[i] - q * y[i + 1])

        a, b = b, r
        i += 1

    return a, x[i], y[i]