# https://projecteuler.net/problem=15
# Clue:
# +------+------+
# |6     |3    1|
# |      |      |
# +------+------+
# |3     |2    1|
# |1     |1    1|
# +------+------+
#
# Pascal triangle
#    1
#   1 1
#  1 2 1
# 1 3 3 1
#1 4 6 4 1
#
# Solved recursively because I dindn't know the pascal triangle formula
#
import sys

cache = {}

def lattice_paths(n, px, py):
    cache_key = '%s_%s' % (px, py)
    if cache_key in cache:
        return cache[cache_key]
    if px == n or py == n:
        result = 1
    else:
      result = lattice_paths(n, px + 1, py) + lattice_paths(n, px, py + 1)
    cache[cache_key] = result
    return result

print lattice_paths(int(sys.argv[1]), 0, 0)