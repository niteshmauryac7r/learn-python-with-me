import functools
import time

@functools.lru_cache(maxsize=None) #memoization technique
def fx(n):
    time.sleep(2)
    return n*5

print(fx(20))
print("done for 20")
print(fx(4))
print("done for 4")
print(fx(2))
print("done for 2")

print(fx(20))
print("done for 20")
print(fx(4))
print("done for 4")
print(fx(2))
print("done for 2")
print(fx(30))
print("done for 30")
