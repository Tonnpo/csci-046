def range(a, b=None, c=None):
    '''
    This function should behave exactly like the built-in range function.
    For example:

    >>> list(range(5))
    [0, 1, 2, 3, 4]
    >>> list(range(1, 5))
    [1, 2, 3, 4]
    >>> list(range(1, 5, 2))
    [1, 3]

    '''
    start = 0 if b is None else a
    stop = a if b is None else b
    step = 1 if c is None else c
    while start != stop:
        if (step > 0 and start > stop) or (step < 0 and start < stop):
            return
        yield start
        start += step
