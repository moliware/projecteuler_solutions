# http://projecteuler.net/index.php?section=problems&id=4

def ispalindrome(n):
    return str(n) == str(n)[::-1]

#Brute force
print max([x*y for x in range(100, 1000) for y in range(100, 1000) if ispalindrome(x*y)])
