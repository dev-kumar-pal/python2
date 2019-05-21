class Salary:
    def __init__(self,pay,bouns):
        self.pay   = pay
        self.bonus = bouns

    def anualSalary(self):
        return (self.pay*12) + self.bonus

class Employee:
    def __init__(self,name,age,salary):
        self.name   = name
        self.age    = age
        self.salary = salary

    def displaySlary(self):
        return self.salary.anualSalary()

sal = Salary(20000,5000)
emp = Employee('Edris',25,sal)
print(emp.displaySlary())