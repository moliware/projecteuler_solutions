# http://projecteuler.net/index.php?section=problems&id=9

abc = 1000
print [a*b*(abc-a-b) for a in xrange(1, abc/3) for b in xrange(a + 1, abc / 2) if a**2+b**2==(abc-a-b)**2]
