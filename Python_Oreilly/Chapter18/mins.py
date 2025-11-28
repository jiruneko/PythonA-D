def min1(*args):
    res = args[0]
    for arg in args[1:]:
        if arg < res:
            res = arg
    return res

def min2(first, *rest):
    for arg in rest:
        if arg < first:
            first = arg
    return first

def min3(*args):
    tmp = list(args)
    tmp.sort()
    return tmp[0]

def min4(*args):
    return sorted(args)[0]

for func in (min1, min2, min3, min4):
    print(func.__name__ + '...')
    print(func(3, 4.0, 1, 2))
    print(func('bb', 'aa'))
    print(func([2, 2], [1, 1], [3, 3]))
    print(func(*'hack'))