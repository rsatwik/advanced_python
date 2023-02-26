# import timeit
# setup_code = '''
# from functools import lru_cache
# from __main__ import fibonacci
# fibonacci_memorized = lru_cache(maxsize=None)(fibonacci)'''

# results = timeit.repeat('fibonacci_memorized(20)',
#                         setup=setup_code,
#                         repeat=1000,
#                         number=1)

# print("Fibonacci cache took {:.5f} us".format(min(results)))


def fibonacci(n):
    if n < 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)