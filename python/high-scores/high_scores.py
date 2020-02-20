

def latest(scores):
    # return last item added to list
    return scores[-1]


def personal_best(scores):
    # max() findes the highest int in list
    return max(scores)


def personal_top_three(scores):
    # make list from low to high
    scores.sort()
    # reverse list
    scores.reverse()
    # return the first 3 list items could also be [0:3]
    return scores[:3]
    