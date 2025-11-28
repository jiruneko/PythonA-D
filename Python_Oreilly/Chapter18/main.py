def f(a, b=2, c=3):
    print(a, b, c)

f(1, 5, 6)


def f(*args):
    print(args)

f(1, 2)

def f(**args):
    print(args)

f(a=1, b=2)


def func(a, *pargs, **kargs):
    print(a, pargs, kargs)

func(1, 2, 3, x=1, y=2)


def accumulate(**kwargs):
    return kwargs

print(accumulate(a=10, b=20, c=30, d=40))