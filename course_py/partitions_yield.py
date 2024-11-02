def plus_minus(x):
    yield x
    yield -x


def evens(start, end):
    even = start + (start % 2)
    while even < end:
        yield even
        even += 2


def countdown(k):
    if k > 0:
        yield k
        yield from countdown(k-1)
    else:
        yield 'Blast off'


def prefixes(s):
    if s:
        yield from prefixes(s[:-1])
        yield s


def substrings(s):
    if s:
        yield from prefixes(s)
        yield from substrings(s[1:])


def count_partitions(n, m):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        with_m = count_partitions(n-m, m)
        without_m = count_partitions(n, m-1)
        return with_m + without_m


def list_partitions(n, m):
    if n < 0 or m == 0:
        return []
    else:
        exact_match = []
        if n == m:
            exact_match = [[m]]
        with_m = [p + [m] for p in list_partitions(n-m, m)]
        without_m = list_partitions(n, m-1)
        return exact_match + with_m + without_m


def partitions(n, m):
    if n > 0 and m > 0:
        if n == m:
            yield str(m)
        for p in partitions(n-m, m):
            yield p + ' + ' + str(m)
        yield from partitions(n, m-1)
