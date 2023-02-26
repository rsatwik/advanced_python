def loop():
    res = []
    for i in range(10000):
        res.append(i * i)
    return sum(res)

def comprehension():
    return sum([i * i for i in range(10000)])

def generator():
    return sum(i * i for i in range(10000))

'''
%timeit loop()
1.09 ms ± 14 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%timeit comprehension()
797 µs ± 16.7 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%timeit generator()
878 µs ± 30 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
'''