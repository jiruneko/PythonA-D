def tracer(func, *pargs, **kwargs):
    print('calling:', func.__name__)
    return func(*pargs, **kwargs)

def func(a, b, c, d):
    return a + b + c + d

print(tracer(func, 1, 2, 3, 4))


def knowly(a, **b):
    print(a, b)
    
knowly(1, b=2)