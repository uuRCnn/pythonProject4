def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(2, 3, 5, 6, 2, 2))


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", colour="Black")
print(my_car.make)
print(my_car.colour)
