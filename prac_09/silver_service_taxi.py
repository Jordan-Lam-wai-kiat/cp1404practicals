from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """SilverServiceTaxi class"""
    def __init__(self, name, fuel, fanciness, flagfall = 4.50, **kwargs):
        """Initialise a Silver service taxi instance, based on parent class Taxi"""
        super().__init__(name, fuel)
        self.fanciness = float(fanciness)
        self.flagfall = flagfall
        self.name = name
        self.fuel = fuel

    def __str__(self):
        """changed string display"""
        return f"{self.name}, fuel={self.fuel}, odo={self._odometer}, {self.current_fare_distance}km on current fare, ${self.scale_price():.2f}/km plus flagfall of ${self.flagfall}"

    def scale_price(self):
        """scale price/km according to fanciness"""
        self.price_per_km = self.fanciness * Taxi.price_per_km
        return self.price_per_km


    def get_fare(self):
        """get fare for distance driven with flagfall included"""
        total_price = self.scale_price() * self.current_fare_distance + self.flagfall
        return round(total_price, 1)
