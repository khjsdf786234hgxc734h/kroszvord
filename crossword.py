#!/usr/bin/python3
import re

with open ('/home/oo/kroszvord/linux.words.lowercase.txt') as f:
    dict = f.read().splitlines()
# regex logical AND
# regex lookahead assertion - this case not needed
pattern = re.compile('(?=.*^[a-z]*$)(?=.*^........h..........$)')
list = list(filter(pattern.match, dict))
print(list)


