# http://projecteuler.net/index.php?section=problems&id=10

import math

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



number = 2000000
# It takes about one hour
print sum(sieve_of_eratosthenes(number))
