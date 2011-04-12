# http://projecteuler.net/index.php?section=problems&id=5
from operator import mul

# Prime list less than 20
prime_list = [1,2,3,5,7,11,13,17,19]
limit = 20
# For each prime calculate the maximum power of that prime less than 20.
# The result is the product of that numbers
print reduce(mul,[p**int(limit ** (1/float(p))) for p in prime_list])