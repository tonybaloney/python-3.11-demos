from _dataklass import dataklass

@dataklass
class Car:
    make: str
    model: str
    engine_capacity: float
    turbo: bool = False


my_car = Car("Audi", "RS4", "2.5", True)
my_car.engine_capacity = 1.2
