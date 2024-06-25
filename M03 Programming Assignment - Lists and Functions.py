# -*- coding: utf-8 -*-

"""
#M03 Programming Assignment - Lists and Functions
#C.J. Becker
#2/5/2024
#Python 3.8.10
#various textbook assignments
"""

#7.4
things = ["mozzarella", "cinderella", "salmonella"]

#7.5
things[1] = "Cinderella"
print(things[1])

#it did change the element

#7.6
things[0] = "MOZZARELLA"
print (things[0])

#7.7
things.pop()
for x in things:
    print(x)

#9.1
def good():
    return ['Harry', 'Ron', 'Hermione']
for x in good():
    print(x)

#9.2
def get_odds():
    oddlist = [0]
    oddlist.pop()
    for x in range(10):
        if x/2 != 0:
            oddlist.append(x)
    return oddlist
print(get_odds()[2])
