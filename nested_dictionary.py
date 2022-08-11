class Vehicles:

    def __init__(self):
        self.data = dict()

    # Defining three getter functions
    def get_items(self):
        return self.data.items()

    def get_keys(self):
        return self.data.keys()

    def get_values(self):
        return self.data.values()

inventory = Vehicles()
inventory.data.update({"Cars": {"Audi": 20, "Mercedes": 32, "BMW": 13}, 'Trucks': {"Mercedes": 5, "Scania": 8}})

# We are calling the getter functions instead of directly accessing the attributes of the object 
items = inventory.get_items()
print(f"Here is the current status of the inventory: {items}.")

keys = inventory.get_keys()
print(f"There are {keys} type of cars in the inventory.")

values = inventory.get_values()
print(f"Here is the number of cars in the inventory: {items}")
