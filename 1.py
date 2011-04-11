# http://projecteuler.net/index.php?section=problems&id=1
#
# Clue:
# Multiples of 3 or 5 = (Multiples of 3 + Multiples of 5) - Multiples of 15

n1 = 5
n2 = 3
n1_and_n2 = n1 * n2
max = 1000

# Number of multiples of each number
n1_multiples = (max - 1) / n1
n2_multiples = (max - 1) / n2
n1_and_n2_multiples = (max - 1) / n1_and_n2

# Multiples of 3 = 3,6,9,12...
# Sum of multiples of 3 = 3*(1+2+3....)
sum_n1 = (n1_multiples * (n1_multiples + 1)) / 2 * n1
sum_n2 = (n2_multiples * (n2_multiples + 1)) / 2 * n2
sum_n1_and_n2 = (n1_and_n2_multiples * (n1_and_n2_multiples + 1)) / 2 * n1_and_n2
print (sum_n1 + sum_n2 - sum_n1_and_n2)
