# http://projecteuler.net/index.php?section=problems&id=14
CACHE = {}
def collatz_problem(n):
    """ Implements Collatz conjecture with a Cache 
    for saving time
    Doc: http://en.wikipedia.org/wiki/Collatz_conjecture
    """
    global CACHE
    if n in CACHE:
        return CACHE[n]
    result = [n]
    while n > 1:
        if n in CACHE:
            n = 1
            result += CACHE[n]
        else:
            n = n/2 if n % 2 == 0 else 3*n + 1
            result.append(n)
    CACHE[n] = result
    return result

limit = 1000000
print max([(x, len(collatz_problem(x))) for x in xrange(2, limit)],key=lambda x:x[1])

