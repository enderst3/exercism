

def latest(scores):
    # return last item added to list
    return scores[-1]


def personal_best(scores):
    # max() findes the highest int in list
    return max(scores)


def personal_top_three(scores):
    # use sorted() to create temp reversed list and return first 3 scores
    # scores.sort() would change the original scores list, we don't want that.
    return sorted(scores, reverse=True)[:3]
    