# https://projecteuler.net/problem=21
# Based on Euler's recursive formula to get sum of divisors.
from itertools import cycle, count, imap, chain, izip

def pentagonal_function(n):
    return (3 * n * n - n) / 2

def pentagonal_sequence():
    """ Sequence 1,-1, 2, -2,..."""
    seq = chain.from_iterable(izip(count(1), count(1)))
    return (i * j for i, j in izip(seq, cycle([1, -1])))

def pentagonal_numbers():
    return imap(pentagonal_function, pentagonal_sequence())

CACHE = {}
def sigma(n):
    if n in CACHE:
        return CACHE[n]
    if n == 1:
        return 1
    else:
        # sigma(n - 1) + sigma(n - 2) - sigma(n - 3) - sigma(n - 5) + ...
        # If the input gets negative you stop. If the input gets zero, then sigma(0)=n. 
        p_numbers = pentagonal_numbers()
        current = n - p_numbers.next()
        acc = 0
        i = 0
        while (current > 0):
            acc += sigma(current) * (1 if (i % 4 < 2) else -1)
            current = n - p_numbers.next()
            i += 1
        if current == 0:
            result = acc + (n * (1 if (i % 4) < 2 else - 1))
            CACHE[n] = result
            return result
        CACHE[n] = acc
        return acc


def amicable_numbers(n):
    d = {i: sigma(i) - i for i in range(1, 10000)}
    result = set()
    for n, sigma_n in d.iteritems():
        if n != sigma_n and sigma_n in d and d[sigma_n] == n:
            result.add(n)
            result.add(sigma_n)
    print sum(result)


if __name__ == '__main__':
    amicable_numbers(10000)
