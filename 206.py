# http://projecteuler.net/index.php?section=problems&id=206
from math import sqrt
import re

# If a square finish in 0 it will finish in 00
until = int(sqrt(1929394959697989900)) + 1
# since = int(sqrt(1020304050607080900)) = 1010101010
# Check with numbers that finish in 030 or 070 because the square
# will finish in 900
since = 1010101030
pattern = '1.2.3.4.5.6.7.8.9.0'

x = since
while (x < until):
    if re.match(pattern, str(x*x)):
        print x
        break
    x += 40 if x % 100 == 30 else 60
