from car import Car

class UnreliableCar(Car):
    def __init__(self, reliability = 49, **kwargs):
        super().__init__(self, **kwargs)
        self.reliability = reliability

    def drive(self, distance):
        from random import uniform
        if self.reliability < uniform(0, 100):
            if distance > self.fuel:
                distance = self.fuel
                self.fuel = 0
            else:
                self.fuel -= distance
            self._odometer += distance
            return distance
        else:
            print("The car didn't start")

my_car = UnreliableCar()
my_car.drive(40)
