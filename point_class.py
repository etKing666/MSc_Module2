class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return (f"x = {self.x}, y = {self.y}")

    def __add__(self, other):
        if isinstance(other, Point):
            return self.add(other)
        else:
            return self.add_tuple(other)


    def add(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return (x, y)

    def add_tuple(self, other):
        x = self.x + other[0]
        y = self.y + other[1]
        return (x,y)

pnt = Point()
pnt.x = 10
pnt.y = 20

a = Point()
a.x = 5
a.y = 5

b = (20, 20)

print(pnt)
print(pnt + b)

