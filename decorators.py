def greet(fx):
    def mfx(*args,**kwargs):
        print("Good Moring")
        result  = fx(*args,**kwargs)
        print("Bye")
        return result
    return mfx

@greet
def hello():
    print("Hello World")
hello()
#greet(hello)()

@greet
def sum(a,b):
    return a+b

sum(1,2)