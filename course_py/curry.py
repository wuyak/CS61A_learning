from operator import add

# def curry2(f):
#    def g(x):
#        def h(y):
#            return f(x, y)
#        return h
#    return g

curry2 = lambda f: lambda x: lambda y: f(x, y)

