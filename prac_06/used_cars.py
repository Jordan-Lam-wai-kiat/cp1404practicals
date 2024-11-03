"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac_06.car import Car

def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180)
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")

    #Part 1
    limo = Car("limo",100)
    #Part 2
    limo.add_fuel(20)
    #Part 3
    print(f"Limo has fuel: {limo.fuel}")
    #Part 4
    limo.drive(115)
    #Part 5 / 6
    print(str(limo))
    #Part 6.5
    limo.add_names("bugatti")
    #Part 7
    print(str(limo))

main()