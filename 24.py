# http://projecteuler.net/index.php?section=problems&id=24

from operator import mul

def fact(x):
    return reduce(mul, range(1, x+1), 1)

def get_nth_perm(objects, n):
    if len(objects) == 1:
        return objects[0]
    n_perms = fact(len(objects) - 1)
    i = n / n_perms
    obj = objects[i]
    new_objects = objects[:]
    new_objects.remove(obj)
    new_n = n - i*n_perms
    return obj + get_nth_perm(new_objects, new_n)

print get_nth_perm(map(lambda x: str(x), range(10)), 10**6 - 1)

    
