def argmax(iterable):
    Imax = 0
    curmax = float("-inf")
    for i, li in enumerate(iterable):
        if li > curmax:
            curmax = li
            Imax = i
    return Imax

def argmin(iterable):
    Imin = 0
    curmin = float("inf")
    for i, li in enumerate(iterable):
        if li < curmin:
            curmin = li
            Imin = i
    return Imin