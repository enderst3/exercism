"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

'''
# Score categories.
# Change the values as you see fit.
YACHT = None
ONES = None
TWOS = None
THREES = None
FOURS = None
FIVES = None
SIXES = None
FULL_HOUSE = None
FOUR_OF_A_KIND = None
LITTLE_STRAIGHT = None
BIG_STRAIGHT = None
CHOICE = None
'''
YACHT = 'YACHT'
ONES = 'ONES'
TWOS = 'TWOS'
THREES = 'THREES'
FOURS = 'FOURS'
FIVES = 'FIVES'
SIXES = 'SIXES'
FULL_HOUSE = 'FULL_HOUSE'
FOUR_OF_A_KIND = 'FOUR_OF_A_KIND'
LITTLE_STRAIGHT = 'LITTLE_STRAIGHT'
BIG_STRAIGHT = 'BIG_STRAIGHT'
CHOICE = 'CHOICE'


def score(dice, category):
    if category == 'YACHT':
        if sum(dice)/5 == max(dice):
            YACHT = 50
            return YACHT
    elif category == 'ONES':
        score = sum(i if i==1 else 0 for i in dice)
        if score > 0:
            ONES = score
            return ONES
    elif category == 'TWOS':
        score = sum(i if i==2 else 0 for i in dice)
        if score > 0:
            TWOS = score
            return TWOS
    elif category == 'THREES':
        score = sum(i if i==3 else 0 for i in dice)
        if score > 0:
            THREES = score
            return THREES
    elif category == 'FOURS':
        score = sum(i if i==4 else 0 for i in dice)
        if score > 0:
            FOURS = score
            return FOURS
    elif category == 'FIVES':
        score = sum(i if i==5 else 0 for i in dice)
        if score > 0:
            FIVES = score
            return FIVES
    elif category == 'SIXES':
        score = sum(i if i==6 else 0 for i in dice)
        if score > 0:
            SIXES = score
            return SIXES
    elif category == 'FULL_HOUSE':
        nums = []
        first_number = False
        second_number = False
        for i in dice:
            if i not in nums and not first_number and dice.count(i) < 4:
                first_number = True
            elif i not in nums and not second_number and dice.count(i) < 4:
                second_number = True
            elif i not in nums:
                break
            nums.append(i)
        else:
            if first_number and second_number:
                FULL_HOUSE = sum(dice)
                return FULL_HOUSE
    elif category == 'FOUR_OF_A_KIND':
        for i in dice:
            if dice.count(i) >= 4:
                FOUR_OF_A_KIND = i*4
                return FOUR_OF_A_KIND
    elif category == 'LITTLE_STRAIGHT':
            for i in [1, 2, 3, 4, 5]:
                if i not in dice:
                    break
            else:
                LITTLE_STRAIGHT = 30
                return LITTLE_STRAIGHT
    elif category == 'BIG_STRAIGHT':
        for i in [2, 3, 4, 5, 6]:
            if i not in dice:
                break
        else:
            BIG_STRAIGHT = 30
            return BIG_STRAIGHT
    elif category == 'CHOICE':
        CHOICE = sum(dice)
        return CHOICE
    return 0