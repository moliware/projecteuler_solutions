# http://projecteuler.net/index.php?section=problems&id=3
import math


def sieve_of_eratosthenes(n):
    """ Return the primes below n
    Doc: http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
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


def find_largest_prime_factor(number):
    """Return the largest prime factor"""
    limit = int(math.sqrt(number))
    prime_list = sieve_of_eratosthenes(limit)
    prime_list.reverse()
    for prime in prime_list:
        if number % prime == 0:
            return prime
    return -1


number = 600851475143
# it takes about 11 minutes
print find_largest_prime_factor(number)
