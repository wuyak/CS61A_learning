class Ratio:
    def __init__(self, n, d):
        self.numer = n
        self.denom = d

    def __repr__(self):
        return f'Ratio({self.numer}, {self.denom})'

    def __str__(self):
        return f'{self.numer}/{self.denom}'

    def __add__(self, other):
        if isinstance(other, int):
            n = self.numer + self.denom * other
            d = self.denom
        elif isinstance(other, Ratio):
            n = self.numer * other.denom + self.denom * other.numer
            d = self.denom * other.denom
        elif isinstance(other, float):
            return float(self) + other
        g = gcd(n, d)
        return Ratio(n//g, d//g)

    def __float__(self):
        return self.numer / self.denom

    __radd__ = __add__

def gcd(n, d):
    while n != d:
        n, d = min(n, d), abs(n-d)
    return n
