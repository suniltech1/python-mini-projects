# Assignment 3: Employee Payroll System
# Approach: Used abstraction with ABC, inheritance for different employee


from abc import ABC, abstractmethod

# Abstract Base Class
class Employee(ABC):
    def __init__(self, name):
        self.name = name

    # Abstract method - must be implemented by all child classes
    @abstractmethod
    def calculate_pay(self):
        pass

    # Common method for all employees
    def payslip(self):
        print(f"{self.name} | Pay: Rs {self.calculate_pay()}")


# Full-Time Employee
class FullTimeEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def calculate_pay(self):
        return self.monthly_salary

    def __str__(self):
        return f"FullTimeEmployee({self.name})"


# Part-Time Employee
class PartTimeEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_pay(self):
        return self.hourly_rate * self.hours_worked

    def __str__(self):
        return f"PartTimeEmployee({self.name})"


# Contractor
class Contractor(Employee):
    def __init__(self, name, project_fee, projects):
        super().__init__(name)
        self.project_fee = project_fee
        self.projects = projects

    def calculate_pay(self):
        return self.project_fee * self.projects

    def __str__(self):
        return f"Contractor({self.name})"


# -------------------------
# Testing


staff = [
    FullTimeEmployee("Asha", monthly_salary=60000),
    PartTimeEmployee("Bibek", hourly_rate=500, hours_worked=80),
    Contractor("Chen", project_fee=15000, projects=3),
]


print("\n=== Payslips ===")
for emp in staff:
    emp.payslip()

print("\n--------------")
# Calculate total payroll
total = sum(e.calculate_pay() for e in staff)

print("Total payroll:", total)



