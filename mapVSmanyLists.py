#@profile
def map_comprehension(numbers):
    a = [n * 2 for n in numbers]
    b = [n ** 2 for n in a]
    c = [n ** 0.33 for n in b]
    return max(c)

@profile
def map_normal(numbers):
    a = map(lambda n: n * 2, numbers)
    b = map(lambda n: n ** 2, a)
    c = map(lambda n: n ** 0.33, b)
    return max(c)

if __name__=="__main__":
    #print(map_comprehension([i for i in range(int(1000))]))
    print(map_normal([i for i in range(int(1000))]))