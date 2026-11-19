#1. úkol (6. 10. 2026)
#Naprogramujte funkci, která pro vstupní přirozené číslo n vrátí hodnotu jeho Eulerovy funkce.
from math import gcd

"""Implementation of Euler's totient function."""

# def gcd(a, b):
#     """Returns the greatest common devider."""
#     while b:
#         a, b = b, a % b
#     return a

def euler_fun(n):
    """Returns the number of numbers lower then n and NSD(a, i) = 1."""
    if n < 1:
        raise ValueError("n must be a positive integer")

    count = 0

    for a in range(1, n):
        if gcd(a, n) == 1:
            count += 1

    return count

if __name__ == "__main__":
    print(euler_fun(32))  # Expected output: 16