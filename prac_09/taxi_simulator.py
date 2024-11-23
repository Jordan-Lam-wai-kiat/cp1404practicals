from silver_service_taxi import SilverServiceTaxi
from taxi import Taxi


taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
print("Let's drive!")
def main(total_bill=0, current_taxi = None):
    valid_option = False
    while valid_option == False:
        print("q)uit, c)hoose taxi, d)rive")
        choice = input(">>> ").lower()
        if choice == "q":
            quit_program(total_bill)
            valid_option = True
        if choice == "c":
            choose_taxi(total_bill)
            valid_option = True
        if current_taxi is None and choice == "d":
            print("You need to choose a taxi before you can drive")
            print(f"Bill to date: ${total_bill:.2f}")
        elif current_taxi is not None and choice == "d":
            drive(total_bill, current_taxi)
            valid_option = True
        if choice not in ["q", "c", "d"]:
            print("Invalid option")
            print(choice)

def choose_taxi(total_bill):
    print("Taxis available:")
    count = 0
    for taxi in taxis:
        print(f"{count} - {taxi}")
        count += 1
    try:
        taxi_choice = int(input("choose_taxi: "))
        current_taxi = taxis[taxi_choice]
        print(f"Bill to date: ${total_bill:.2f}")
        return main(total_bill, current_taxi)
    except IndexError:
        print("Invalid taxi choice")
        print(f"Bill to date: ${total_bill:.2f}")
        return main(total_bill, None)


def drive(total_bill, current_taxi):
    distance_driven = int(input("Dive how far? "))
    current_taxi.drive(distance_driven)
    print(f"Your {current_taxi.name} trip will cost you ${current_taxi.get_fare():.2f}")
    total_bill += float(current_taxi.get_fare())
    print(f"Bill to date: ${total_bill:.2f}")
    return main(total_bill, None)

def quit_program(total_bill):
    print(f"Total trip cost: ${total_bill}")
    print("Taxis are now:")
    count = 0
    for taxi in taxis:
        print(f"{count} - {taxi}")
        count += 1

main()