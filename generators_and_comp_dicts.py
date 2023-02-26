def loop():
    res = {}
    for i in range(10000):
        res[i] = i
    return res

def comprehension():
    return {i: i for i in range(10000)}


'''
%timeit loop()
800 µs ± 13.2 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%timeit comprehension()
689 µs ± 10.4 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
'''