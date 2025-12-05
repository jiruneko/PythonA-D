import time
timer = time.perf_counter

def once(func, *pargs, **kwargs):
    start = timer()
    result = func(*pargs, **kwargs)
    elapsed = timer() - start
    return (elapsed, result)

def total(reps, func, *pargs, **kargs):
    total = 0
    for i in range(reps):
        time, result = once(func, *pargs, **kargs)
        total += time
    return (total, result)

def bestof(reps, func, *pargs, **kargs):
    return min(once(func, *pargs, **kargs) for i in range(reps))

def bestpftotal(reps1, reps2, func, *pargs, **kargs):
    return min(total(reps2, func, *pargs, **kargs) for i in range(reps1))