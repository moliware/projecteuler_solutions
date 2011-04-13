# http://projecteuler.net/index.php?section=problems&id=40
from operator import mul

#It's sure that if it counts until 1000000 it has more than 1000000 digits
d = ''.join([str(x) for x in range(0,1000001)])
print reduce(mul,[int(d[10**i])for i in range(7)])
