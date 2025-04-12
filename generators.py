def my_gen():
    for i in range(200):
        yield i

gen = my_gen()
print(next(gen))
print(next(gen))
print(next(gen))
