""" Write a Python program to achieve basic employee-related functionality which includes retaining
employee details and allowing an employee to book a day of annual leave. Extend the Python program
you have now created to use protected and unprotected variables. """

from datetime import date

class Employee():
    _company = "Acme"

    def __init__(self, name, surname, dept):
        self.name = name
        self.surname = surname
        self.dept = dept

    def leave(self):
        self.year = input("Enter the year of leave:")
        self.month = input("Enter the month of leave:")
        self.day = input("Enter the day of leave:")
        return print(f"You asked for a leave on {self.day}/{self.month}/{self.year}")

Tom = Employee("Tom", "Blackwood", "Accounting")
#Tom.name = "Tom"
#Tom.surname = "Blackwood"
#Tom.dept = "Accounting"

print(f"{Tom.name} {Tom.surname} from {Tom.dept}")
Tom.leave()