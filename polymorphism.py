# An example of polymorphism (method overriding):

class Vehicle():

    def __init__(self, type, velocity, direction, lane):
        self.type = type
        self.velocity = velocity
        self.direction = direction
        self.lane = lane

    def print_state(self):
        print(f"The vehicle's velocity is {self.velocity} km/h, direction is {self.direction} and it is on lane {self.lane}.")

# Vehicle types: 1. Automobile 2. SUV 3. Van 4. Truck 5. Other

class Car(Vehicle):

    def print_state(self):
        print(f"The car's velocity is {self.velocity} km/h, direction is {self.direction} and it is on lane {self.lane}.")

class Truck(Vehicle):

    def print_state(self):
        print(f"The truck's velocity is {self.velocity} km/h, direction is {self.direction} and it is on lane {self.lane}.")

# Here, we have overridden the parent class' print_state() function in the child classes (Car and Truck).
# However, we still call the method by the same name, even though it behaves (slightly) different. Note the small
# difference in the output. This is a type of polymorphism, namely "method overriding".

Audi = Car(1, 60, "N", 2)
Scania = Truck(4, 30, "W", 1)

for vehicle in (Audi, Scania):
    vehicle.print_state()
    
