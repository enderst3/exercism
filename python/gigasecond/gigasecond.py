
# import timedelta
from datetime import timedelta

def add(moment):
    # add the gigaseconds to the moment using timedelta
    return moment + timedelta(seconds=10**9)