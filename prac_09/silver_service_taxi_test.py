from silver_service_taxi import SilverServiceTaxi

new_taxi = SilverServiceTaxi("silver taxi", 2)
assert new_taxi
print(new_taxi)
new_taxi.drive(18)
print(new_taxi)
