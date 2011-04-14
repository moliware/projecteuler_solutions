# http://projecteuler.net/index.php?section=problems&id=35

import math


def sieve_of_eratosthenes(n):
    """ Return the primes below n"""
    if n <= 0:
        return []
    if n == 1:
        return [1]
    vector = range(n, 1, -1)
    current_prime = vector.pop()
    result = {}
    result[current_prime]=1
    while vector:
        vector = [c for c in vector if c % current_prime != 0]
        current_prime = vector.pop()
	result[current_prime] = 1
    return result

def get_posible_rotations(number):
    result = [number]
    current = str(number)
    for x in range(len(current) - 1):
        current = current[-1] + current[0:len(current) - 1]
        result.append(int(current))
    return result

def is_circular(prime, prime_hash):
    rotations = get_posible_rotations(prime)
    for rotation in rotations:
        if rotation not in prime_hash:
            return False
    return True

number = 1000000
prime_hash = sieve_of_eratosthenes(number)

print len([prime for prime in prime_hash.keys() if is_circular(prime, prime_hash)])
