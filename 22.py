# http://projecteuler.net/index.php?section=problems&id=22
from urllib2 import urlopen
import re

names_str = urlopen('http://projecteuler.net/project/names.txt').read()
names = re.sub('"', '', names_str).split(',')
names.sort()
print sum([reduce(lambda x,y: x+ord(y) - ord('A') + 1, name, 0) * (i+1) for i, name in enumerate(names)])

