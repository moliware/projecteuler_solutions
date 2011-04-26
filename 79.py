# http://projecteuler.net/index.php?section=problems&id=79

from urllib2 import urlopen

numbers = set(urlopen('http://projecteuler.net/project/keylog.txt').read().split())
passwd = ''
while numbers:
    first_digits = set([number[0] for number in numbers])

    to_remove = set([])
    for number in numbers:
        for digit in first_digits:
            if digit in number[1:]:
                to_remove.add(digit)
    [first_digits.remove(digit) for digit in to_remove]
    digit = first_digits.pop()
    if not digit:
        raise Exception
    new_numbers = set([])
    for number in numbers:
        if digit == number[0]:
            if number[1:]:
                new_numbers.add(number[1:])
        else:
            new_numbers.add(number)
    numbers = new_numbers
    passwd += digit
print passwd
