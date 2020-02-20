'''
on every year that is evenly divisible by 4
  except every year that is evenly divisible by 100
    unless the year is also evenly divisible by 400
'''


def leap_year(year):
    # check if divisible by 4
    if year % 4 == 0:
        # check if divisible by 100
        if year % 100 == 0:
            # check if divisble by 400
            if year % 400 == 0:
                # if yes return true
                return True
            # if no return false
            return False
        # if no return true
        return True 
    # if no return false
    return False