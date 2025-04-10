import time

timings = []
timing = {}
def t_time(fx):
    def mfx(*args,**kwargs):
        start_time = time.time()
        result = fx(*args,**kwargs)
        end_time = time.time()
        total_time = end_time - start_time
        timings.append(f"{total_time:.2}")
        timing[fx.__name__] = (f"{total_time:.2}")
        
        return result
    return mfx

@t_time
def withwhile():
    i = 0
    while i < 50000:
        i = i+1
        
        

@t_time
def withfor():
    i=0
    for i in range(50000):
        i = i+1
        

withwhile()
withfor()

print(timings)
time.sleep(4)
for key , value in timing.items():
    print(key,value)


formatted_time = time.strftime("%y-%m-%d %H:%M:%S")
print(formatted_time)