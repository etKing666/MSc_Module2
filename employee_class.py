"""Instructions: Develop a class diagram using UML to support a system with basic employee-related functionality.
This should include the retention of employee details and allowing an employee to book a day of annual leave.
Develop the Python program to implement the class model."""

class Employee:
    def __init__(self, name, surname, position, rem_leave=30):
        self.name = name
        self.surname = surname
        self.position = position
        self.rem_leave = rem_leave  # Remaining leave

class Employer:
    def __init__ (self, employees=None):
        self.employees = []

    def add_employee(self, Person):  # Adds employee to the list of employees
        self.employees.append(Person)

    def book_leave(self, Person, days):  # Books leave for the employer
        if Person.rem_leave == 0:
            print("You have no leave left this year.")
        else:
            leave = Person.rem_leave
            Person.rem_leave = leave - days
            print(f"You booked {days} of leave. You have {Person.rem_leave} days of leave left.")

manager = Employee ('John', 'Doe', 'Manager')
employer = Employer()
employer.add_employee(manager)
employer.book_leave(manager, 10)