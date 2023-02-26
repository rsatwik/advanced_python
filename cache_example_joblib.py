from joblib import Memory
memory = Memory(cachedir='cache')

@memory.cache
def sum2(a, b):
    print("Calculating {} + {}".format(a,b))
    return a+b

print(sum2(1,2))
print()
print(sum2(1,2))