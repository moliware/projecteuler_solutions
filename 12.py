# http://projecteuler.net/index.php?section=problems&id=12
import math
from operator import mul

def fermat_factor(n):
    # Method for calculate a divisor of and odd int
    # http://en.wikipedia.org/wiki/Fermat%27s_factorization_method
    # Note: when n is prime always return 1
    a = math.ceil(math.sqrt(n))
    b2 = a**2 - n
    while math.sqrt(b2) != int(math.sqrt(b2)):
        a +=1
        b2 = a**2 - n
    return int(a - math.sqrt(b2))

def factorize(n):
    factors = {}
    while (n != 1):
        if n % 2 == 0:
            factor = 2
        else:
            # odd integer
            factor = fermat_factor(n)
            # Factor cannot be a prime
            # This is not a good way for check if a number is a prime
            # but it works :)
            is_prime = fermat_factor(factor)
            while(is_prime != 1):
                factor = is_prime
                is_prime = fermat_factor(factor)
        if factor == 1:
            factors[n] = factors[n] + 1 if n in factors else 1
            break
        else:
            factors[factor] = factors[factor] + 1 if factor in factors else 1
            n /= factor
    return factors.items()

def num_factors(factors):
    # 28 = 2^2*7^1 num_divisors = (2+1)*(1+1)
    return reduce(mul, [x[1] + 1 for x in factors], 1)

def triangle_numbers():
    n = 1
    while True:
        yield (n * (n +1))/2
        n +=1


for n in triangle_numbers():
    if num_factors(factorize(n)) > 500:
        print n
        break
