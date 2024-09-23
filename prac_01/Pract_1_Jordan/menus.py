name = input("Enter name: ")
menu = """Please input an option you would like to choose using the first alphabet of each choice: \n (H)ello \n (G)oodbye \n (Q)uit"""
print(menu)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print("Hello", name)
    elif choice == "G":
        print("Goodbye", name)
    else:
        print("invalid choice")
    print(menu)
    choice = input(">>> ").upper()
print("Finished.")