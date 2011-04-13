# http://projecteuler.net/index.php?section=problems&id=20

from operator import mul

n = 100
print sum([int(x) for x in str(reduce(mul, range(1,n+1)))])
