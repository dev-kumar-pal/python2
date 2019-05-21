'''class Person:
    def __init__(self,name,age):
        self.name = name
        self.age  = age

p =Person('Edris',25)
p.age = 50
print(p.name)
print(p.age)'''

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age  = age

    def setName(self,name):
        self.__name = name

    def getName(self):
        return self.__name

    def setAge(self, age):
        self.__age = age

    def getAge(self):
        return self.__age

p = Person('Edris',25)

'''p.__name = 'Hello'
p.__age  = 40
print(p.__name)
print(p.__age)

print(p.getName())
print(p.getAge())'''

print(p.getName())
print(p.getAge())
