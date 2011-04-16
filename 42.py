# http://projecteuler.net/index.php?section=problems&id=42

from urllib2 import urlopen
import re

def triangle_numbers(n):
    """ Triangle numbers before n"""
    triangle_nums = {}
    current = 0
    i = 1
    while current + i < n:
        current += i
        triangle_nums[current] = 1
        i+=1
    return triangle_nums

def alphabetical_position(char):
    return ord(char.upper()) - ord('A') + 1
def word_number(word):
    return sum(map(alphabetical_position, word))

words = re.findall('"(\w*?)"', urlopen('http://projecteuler.net/project/words.txt').read())

max_word_length =  len(max(words, key=lambda x: len(x)))
triangle_hash = triangle_numbers(alphabetical_position('Z') * max_word_length)
print len([word for word in words if word_number(word) in triangle_hash])
