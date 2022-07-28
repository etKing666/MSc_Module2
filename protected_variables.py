class Person():

    def __init__(self, name, surname, salary):
        """Since name is not a personal identifier attribute (e.g. there can be thousands of people named "Paul") we do
        not want the name variable to be protected. However, when it comes together with surname it may be personal
        identifier. So, we do not want anybody to directly access it and make it protected. Salary is perhaps the
        most sensitive data here, so we went one step further and made it private. """
        self.name = name # Unprotected attribute
        self._surname = surname # Protected attribute
        self.__salary = salary # Private attribute


# Instantiate the Person() class:
person1 = Person("Etkin", "Getir", 1000)
print(person1.name)

# Note that "_" is just a convention, and we can still access protected attributes directly.
print(person1._surname)

# However, when we make it private with "__", it is not possible to access the attribute directly. Hence, this will
# raise an error:
# print(person1.__salary)
# But it can still be reached (that's another story). Try this:
# print(person1._Person__salary)



