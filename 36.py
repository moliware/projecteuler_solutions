# http://projecteuler.net/index.php?section=problems&id=36

def ispalindromic(s):
    return s == s[::-1]
n = 1000000
print sum([x for x in xrange(n) if ispalindromic(str(x)) and ispalindromic(bin(x)[2:])])
