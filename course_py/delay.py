from operator import add, mul
def square(x):
    return mul(x, x)

def delay(arg):
    print('delayed')

    def g():
        return arg
    return g


a = delay(delay)()(6)()
print(a, '\nend')
b = print(delay(print)()(4))
print(b, '\nend')

def pirate(arggg):
    print('matey')

    def plunder(arggg):
        return arggg
    return plunder


c = add(pirate(3)(square)(4), 1)
print(c, '\nend')
