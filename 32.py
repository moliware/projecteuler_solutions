# https://projecteuler.net/problem=32
from itertools import permutations

def is_pandigital(x, y, z):
    concat_number = "%d%d%d" % (x, y, z)
    return ''.join(sorted(concat_number)) == ''.join(map(str,range(1,10)))

def calculate_products():
    """ The only products that can reach 9 digits in total are:
    _ x _ _ _ _ = _ _ _ _ _
    _ _ x _ _ _ = _ _ _ _ _
    """
    products = set()
    for n_digits in [1, 2]:
        for multiplicand_perm in permutations(range(1, 10), n_digits):
            multiplicand = int(''.join(map(str, multiplicand_perm)))
            l = range(1, 10)
            [l.remove(x) for x in multiplicand_perm]
            for multiplier_perm in permutations(l, 5 - n_digits):
                multiplier = int(''.join(map(str, multiplier_perm)))
                product = multiplicand * multiplier
                if (is_pandigital(multiplicand, multiplier, product)):
                    print '%d * %d = %d' % (multiplicand, multiplier, product)
                    products.add(product)
    return products

if __name__ == '__main__':
    print sum(calculate_products())
