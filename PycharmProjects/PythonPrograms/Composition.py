class Salary:
    def __init__(self,pay,bouns):
        self.pay   = pay
        self.bonus = bouns

    def anualSalary(self):
        return (self.pay*12) + self.bonus

class Employee:
    def __init__(self,name,age,pay,bonus):
        self.name   = name
        self.age    = age
        self.salary = Salary(pay,bonus)

    def displaySlary(self):
        return self.salary.anualSalary()

emp = Employee('Edris',25,20000,5000)
print(emp.displaySlary())