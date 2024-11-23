from taxi import Taxi

class SilverServiceTaxi(Taxi):
    def __init__(self, name, fanciness, fuel=200, flagfall = 4.50, **kwargs):
        super().__init__(name=name, fuel=fuel, **kwargs)
        self.fanciness = float(fanciness)
        self.flagfall = flagfall
        self.name = name
        self.fuel = fuel

    def __str__(self):
        return f"{self.name}, fuel={self.fuel}, odo={self._odometer}, {self.current_fare_distance}km on current fare, ${self.scale_price():.2f}/km plus flagfall of ${self.flagfall} \n Total fare: ${super().get_fare() + self.flagfall:.2f}"

    def scale_price(self):
        """scale price/km according to fanciness"""
        self.price_per_km = self.fanciness * Taxi.price_per_km
        return self.price_per_km


    def get_fare(self):
        total_price = self.scale_price() * self.current_fare_distance
        return f"${total_price}"
