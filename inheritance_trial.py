# Super class for cars
class Cars:
    def __init__(self, cartype, make, model, year):
    # Since we do not want the type of the vehicle to be changed, we will use a protected variable
        self.__cartype = 'Automobile'
        self.make = make
        self.model = model
        self.year = year

# Let's create two subclasses that inherit from super class Cars. In this case, country will be protected:
class GermanCar(Cars):
    def __init__ (self, cartype, make, model, year, _country):
        Cars.__init__(self, cartype, make, model, year)
        self._country = 'Germany'


class ItalianCar(Cars):
    def __init__ (self, cartype, make, model, year, _country):
        Cars.__init__(self, cartype, make, model, year)
        self._country = 'Italy'

car1 = GermanCar()
car1.make = 'Audi'
car1.model = 'A3'
car1.year = 2018

car2 = ItalianCar()
car2.make = 'Alfa Romeo'
car2.model = 'Giulietta'
car2.year = 2015

print(car1)
print(car2)
