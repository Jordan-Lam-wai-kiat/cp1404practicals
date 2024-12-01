from car import Car

class UnreliableCar(Car):
    """UnreliableCar class"""
    def __init__(self, reliability = 49, **kwargs):
        """Initialise a unreliable car instance, based on parent class Car."""
        super().__init__(self, **kwargs)
        self.reliability = reliability

    def drive(self, distance):
        """Drive like parent Car but checks if reliability is high enough to start driving"""
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