def add(*args):
    print(args[1])
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(1 , 2, 3, 4, 5))

def calculate(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key, value)



calculate(add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        # self.make = kw["make"]
        # self.model = kw["model"]
        self.make = kw.get("make")  #hvis denne ikke findes returneres none
        self.model = kw.get("model") #hvis denne ikke findes returneres none
        self.year = kw.get("year")
        self.color = kw.get("color")
        self.range = kw.get("range")

# my_car = Car(make="Volkswagen", model="ID2")
my_car = Car(make="Volkswagen", color="Black")
print(my_car.make, my_car.color)