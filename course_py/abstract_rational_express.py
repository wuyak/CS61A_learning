# Rational arithmetic


def rational(n, d):
    def select(name):
        if name == 'n':
            return n
        elif name == 'd':
            return d
    return select


def numer(x):
    return x('n')


def denom(x):
    return x('d')


def add_rational(x, y):
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return rational(nx * dy + ny * dx, dx * dy)


def mul_rational(x, y):
    return rational(numer(x) * numer(y), denom(x) * denom(y))


def rationals_are_equal(x, y):
    return numer(x) * denom(y) == numer(y) * denom(x)


def print_rational(x):
    print(numer(x), "/", denom(x))


x, y = rational(1, 2), rational(3, 8)
