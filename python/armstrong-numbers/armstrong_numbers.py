def is_armstrong_number(number):
    # create list of digits mulitiplied by the power of len.
    digits = [int(d)**len(str(number)) for d in str(number)]
    
    # Check if the two numbers equal each other
    if sum(digits) != number:
        return False
    return True

'''
# as a for loop it would be 
digits = []
for d in str(number):
    digits.append(int(d)**len(str(number)))

'''