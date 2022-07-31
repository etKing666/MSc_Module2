from abc import ABC, abstractmethod

# Creating an abstract base class for all vehicles in the system
class Vehicles(ABC):
    

class Vehicle():

    def __init__(self, type, velocity, direction, lane):
        self.type = type
        self.velocity = velocity
        self.direction = direction
        self.lane = lane

# Vehicle types: 1. Automobile 2. SUV 3. Van 4. Truck 5. Other

# Setting up the userbase as a set (because it is the easiest way to test membership, since it doesn't allow duplicates:
userbase =("etking", "olib")

class Car(Vehicle):

    def print_state(self):
        print(f"The car's velocity is {self.velocity} km/h, direction is {self.direction} and it is on lane {self.lane}.")

class User():

    def __init__(self, name, surname, username):
        self.name = name
        self.surname = surname
        self.username = username

    def turn_on(self, Control_Unit):
        if Control_Unit.status == False:
            if Control_Unit.auth_status == True:
                Control_Unit.status = True
                print("The car has been turned on.")
            else:
                print("The user is not authenticated!")

class Control_Unit():

    def __init__(self, status=False, auth_status=False):
        self.status = status
        self.auth_status = auth_status

    def obstacles(self, obstacles):
        self.obstacles = obstacles

    def status(self, status=False):
        self.status = status

    def auth(self, user):

        if user in userbase:
            print("The user has been authenticated.")
            self.auth_status=True
        else:
            print("User is not found.")


# For debugging

user1 = User("Etkin", "Getir", "etking")
cunit = Control_Unit()
user1.turn_on(cunit)
print(cunit.status)
cunit.auth(user1.username)
user1.turn_on(cunit)