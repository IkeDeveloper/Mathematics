import pygame
class Person:
    def __init__(self, age, weight, height, first_name, last_name, address, department, salary):
        self.age = age
        self.weight = weight
        self.height = height
        self.first_name=first_name
        self.last_name=last_name
        self.address = address
        self.department=department
        self.salary=salary

    def getage(self):
        return f"{user.age}"

    def getweight(self):
        return f"{user.weight}"

    def getname(self):
        return f"{user.first_name+" "+user.last_name}"

    def getaddress(self):
        return f"{user.address}"

    def getdepartment(self):
        return f"{self.department}"

    def getsalary(self):
        return f"{self.salary}"

    def raisesalary(self,percentage):
        self.salary=self.salary*(100+percentage)/100

user = Person(53,95,190,"Ike","Muoma", "21 Cobham Road","Accounts",32000)

employeeage=user.getage()
employeeweight=user.getweight()
employeeheight=user.getname()
employeeaddress=user.getaddress()
employeedep=user.getdepartment()

user.raisesalary(10)
employeesalary = user.getsalary()
print(employeeage, employeeweight, employeeheight,employeeaddress,employeedep, employeesalary)







