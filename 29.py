# https://projecteuler.net/problem=29
from itertools import chain

print len(set(chain.from_iterable([[ i ** j for j in range(2,101)] for i in range(2,101)])))