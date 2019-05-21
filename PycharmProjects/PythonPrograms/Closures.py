def printer(name):
    def printName():
        print(name)
    return printName

opt = printer("Edris")
del printer
#printer("Hello")
opt()
