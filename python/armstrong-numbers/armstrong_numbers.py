def is_armstrong_number(number):
    # create list to store numbers to add
    digits = []
    # loop through digits in number and multiply by lenth, then add to list
    for d in str(number):
        digits.append(int(d)**len(str(number)))
    # Check if the two numbers equal each other
    if sum(digits) != number:
        return False
    return True