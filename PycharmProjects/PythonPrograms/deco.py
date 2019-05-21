def fun(func):
    def fun1():
        print("*******")
        func()
        print("*******")
    return fun1

def fun2():
    print("Edris")

decor = fun(fun2)
decor()