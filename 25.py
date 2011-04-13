# http://projecteuler.net/index.php?section=problems&id=25

Fi = 1
Fj = 1
i = 2
while len(str(Fj)) < 1000:
    Fnext = Fi + Fj
    Fi = Fj
    Fj = Fnext
    i += 1
# Fi is the lats term to contain less than 1000 digits
print i

