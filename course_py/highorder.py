def apply_twice(f, x):
    return f(f(x))

def square(x):
    return x * x

def make_adder(n):
    def adder(k):
        return k + n
    return adder

def square(x):
    return x * x

def triple(x):
    return x * 3

def compose1(f, g):
    def h(x):
        return f(g(x))
    return h
