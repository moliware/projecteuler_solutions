# https://projecteuler.net/problem=92

def square_of_digits(n):
    return sum(int(x) ** 2 for x in str(n))


cache = {}


def arrive_at_89(n):
    if n in cache:
        return cache[n]
    elif n == 89:
        return True
    elif n == 1:
        return False
    else:
        cache[n] = arrive_at_89(square_of_digits(n))
        return cache[n]


print len(list(x for x in range(1, 10 ** 7 + 1) if arrive_at_89(x)))