class Employee:
    def __init__(self, name, salary, emp):
        self.name = name
        self.salary = salary
        self.emp = emp

    def get_info(self):
        return f"Employee {self.name}, salary {self.salary}, emp {self.emp}"

class Manager(Employee):
    def get_info(self):
        return f"Manager {self.name}, salary {self.salary}, emp {self.emp}"

class SoftwareEngineer(Employee):
    def __init__(self, language, name, salary, emp):
        super().__init__(name, salary, emp)
        self.language = language
    def get_info(self):
        return f"Software Engineer {self.name}, salary {self.salary}, emp {self.emp}, language {self.language}"


employees = [
    Manager("Vera", 2000,1),
    Employee("Chuck", 1800,2),
    Employee("Dave", 1900,3),
    SoftwareEngineer("Cobol","Ike",10000,4)
]

for e in employees:
    print(e.get_info())