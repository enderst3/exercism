'''
Perfect: aliquot sum = number
    6 is a perfect number because (1 + 2 + 3) = 6
    28 is a perfect number because (1 + 2 + 4 + 7 + 14) = 28
Abundant: aliquot sum > number
    12 is an abundant number because (1 + 2 + 3 + 4 + 6) = 16
    24 is an abundant number because (1 + 2 + 3 + 4 + 6 + 8 + 12) = 36
Deficient: aliquot sum < number
    8 is a deficient number because (1 + 2 + 4) = 7
    Prime numbers are deficient
'''


def classify(number):
    factors = [i for i in range(1, number) if number%i==0]
    if number < 1 or number % 1 != 0:
        raise ValueError('{} is not a natual number.'.format(number))

    if sum(factors) > number:
        return "abundant"
    if sum(factors) < number:
        return "deficient"
    return 'perfect'
    