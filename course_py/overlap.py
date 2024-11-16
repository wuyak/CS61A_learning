
def overlap(s, t):
    """For increasing s and t, count the numbers that appear in both.

    >>> a = Link(3, Link(4, Link(6, Link(7, Link(9, Link(10))))))
    >>> b = Link(1, Link(3, Link(5, Link(7, Link(8)))))
    >>> overlap(a, b)  # 3 and 7
    2
    >>> overlap(a.rest, b)  # just 7
    1
    >>> overlap(Link(0, a), Link(0, b))
    3
    """
    "*** YOUR CODE HERE ***"
#    count = 0
#    while s:
#        temp_t = t
#        while temp_t:
#            if s.first == temp_t.first:
#                count += 1
#                break
#            temp_t = temp_t.rest
#        s = s.rest
#    return count

    if s is Link.empty:
        return 0
    return 1 + overlap(s.rest, t) if overlap_helper(s.first, t) else overlap(s.rest, t)


def overlap_helper(value, t):
    if t is Link.empty:
        return False
    if t.first == value:
        return True
    return overlap_helper(value, t.rest)
