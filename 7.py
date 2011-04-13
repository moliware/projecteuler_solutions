# http://projecteuler.net/index.php?section=problems&id=7

import math
import time

def PNT(x):
    """prime number theorem (PNT): that gives the number of primes less than or equal to x,
    for any real number x. 
    Doc: http://en.wikipedia.org/wiki/Prime_number_theorem
    """
    return float(x) / math.log(x)

def find_x(pnt_x):
    x = 2
    while PNT(x) < pnt_x:
        x *= 2
    return x

def sieve_of_eratosthenes(n):
    """ Return the primes below n
    Doc : http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    """
    if n <= 0:
        return []
    if n == 1:
        return [1]
    vector = range(n, 1, -1)
    current_prime = vector.pop()
    result = [current_prime]
    while vector:
        vector = [c for c in vector if c % current_prime != 0]
        current_prime = vector.pop()
        result.append(current_prime)
    return result


n = 10001
x = find_x(n)
print sieve_of_eratosthenes(x)[n - 1]
