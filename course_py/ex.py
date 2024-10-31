def plus_minus(x):
    yield x
    yield -x


def evens(start, end):
    even = start + (start % 2)
    while even < end:
        yield even
        even += 2
