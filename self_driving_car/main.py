class Vehicle():

    def __init__(self, type, velocity, direction, lane):
        self.type = type
        self.velocity = velocity
        self.direction = direction
        self.lane = lane

# Vehicle types: 1. Automobile 2. SUV 3. Van 4. Truck 5. Other

class Car(Vehicle):

    def print_state(self) -> object:
        print(f"The car's velocity is {self.velocity} km/h, direction is {self.direction} and it is on lane {self.lane}.")

Audi = Car(1, 60, "N", 2)

Audi.print_state()

