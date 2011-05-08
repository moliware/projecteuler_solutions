# http://projecteuler.net/index.php?section=problems&id=2

def fibonacci(limit):
    n_2 = 0
    n_1 = 1
    while(limit > n_2 + n_1):
        n = n_2 + n_1
        yield n
        n_2 = n_1
        n_1 = n
print sum([x for x in fibonacci(4000000) if x % 2 == 0])

