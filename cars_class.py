class Cars:
    def __init__(self, cartype, make, model, year):
    # Since we do not want the type of the vehicle to be changed, we will use a protected variable
        self._cartype = 'Automobile'
        self.make = make
        self.model = model
        self.year = year

car1 = Cars()
car1.make = 'Audi'
car1.model = 'A3'
car1.year = 2018


print(car1)