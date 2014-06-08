# https://projecteuler.net/problem=34
import math

factorials = {str(i): math.factorial(i) for i in range(10)}

def is_curious_number(n):
    # print n
    return n == sum(factorials[x] for x in str(n))

# let's say 9.999.999 is the upper limit since 9! * 7 < 9.999.999
print sum(i for i in range(10, 10 ** 7) if is_curious_number(i))