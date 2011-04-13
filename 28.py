# http://projecteuler.net/index.php?section=problems&id=28

spiral = [1,3,5,7,9]
step = 10
dimension = 1001
for x in range(len(spiral), 2 * dimension - 1):
    spiral.append(spiral[x - 4] + step)
    step += 2

print sum(spiral)
