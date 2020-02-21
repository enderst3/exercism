def slices(series, length):
    # If length is longer than series or lenth is 0 or empty
    if length > len(series) or length < 1:
        # raise exception
        raise ValueError('Invalid length or, No length')
    # create list of slices, using for loop. Subtract length +1 to keep from getting shorter lenth slices
    slice = [series[i:i+length] for i in range(len(series)-length+1)]
    return slice
