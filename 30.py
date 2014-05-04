# https://projecteuler.net/problem=30
# Clue:
# It's impossible to get a number of 7 digits because (9 ** 5) * 7 = 413343
# and that number has 6 digits

def check(n, index):
    int_list = [int(x) ** index for x in str(n)]
    return sum(int_list) == n

print sum([n for n in xrange(2, 999999) if check(n, 5)])
