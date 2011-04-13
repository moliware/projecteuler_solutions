# http://projecteuler.net/index.php?section=problems&id=6

def sum_of_the_squares(n): return sum([x * x for x in range(1, n+1)])
def square_of_the_sum(n): return sum(range(1, n+1)) ** 2

print square_of_the_sum(100) - sum_of_the_squares(100)
