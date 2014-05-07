# https://projecteuler.net/problem=17



reference = {
    1: len("one"),
    2: len("two"),
    3: len("three"),
    4: len("four"),
    5: len("five"),
    6: len("six"),
    7: len("seven"),
    8: len("eight"),
    9: len("nine"),
    10: len("ten"),
    11: len("eleven"),
    12: len("twelve"),
    13: len("thirteen"),
    14: len("fourteen"),
    15: len("fifteen"),
    16: len("sixteen"),
    17: len("seventeen"),
    18: len("eighteen"),
    19: len("nineteen"),
    20: len("twenty"),
    30: len("thirty"),
    40: len("forty"),
    50: len("fifty"),
    60: len("sixty"),
    70: len("seventy"),
    80: len("eighty"),
    90: len("ninety")
}
one_digit = sum(reference[i] for i in range(1, 10))
teens = sum(reference[i] for i in range(10, 20))
two_digits = teens + sum(reference[i * 10] * 10 for i in range(2, 10)) + (8 * one_digit)
three_digits = (9 * one_digit) + (9 * two_digits) + (99 * 9 * len("and")) + sum((reference[i] + len("hundred")) * 100 for i in range(1, 10))
print one_digit + two_digits + three_digits + len("one") + len("thousand")