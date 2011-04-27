# http://projecteuler.net/index.php?section=problems&id=97

print str(reduce(lambda x,y: 2*x % 10**10, range(7830457), 1) * 28433 + 1)[-10:]
