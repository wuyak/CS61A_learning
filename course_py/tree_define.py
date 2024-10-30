__all__ = ['tree', 'label', 'branches', 'is_tree', 'is_leaf', 'fib_tree', 'increment_leaves', 'print_tree']

def tree(label, branches=[]):
    return [label] + list(branches)

def label(t):
    return t[0]

def branches(t):
    return t[1:]

def is_tree(t):
    return isinstance(t, list) and len(t) > 0

def is_leaf(t):
    return len(branches(t)) == 0

def fib_tree(n):
    if n <= 1:
        return tree(n)
    else:
        left, right = fib_tree(n-2), fib_tree(n-1)
        return tree(label(left) + label(right), [left, right])

def increment_leaves(t):
    if is_leaf(t):
        return tree(label(t) + 1)
    else:
        return tree(label(t), [increment_leaves(b) for b in branches(t)])

def print_tree(t, indent=0):
    print(' ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)
