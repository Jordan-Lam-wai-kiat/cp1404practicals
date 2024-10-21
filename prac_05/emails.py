input_email = " "
credentials_dict = {}
while input_email != "":
    input_email = input("Email: ")
    if input_email != "":
        credentials_dict[input_email] = ([word for word in input_email.split("@")][0]).title()
        validate_name = input(f"Is your name {credentials_dict[input_email]}? (Y/N)").lower()
        if validate_name == "n":
            change_name = input("Name: ")
            credentials_dict[input_email] = change_name
        else:
            continue
print("\n")
for email, name in credentials_dict.items():
    print(f"{name} ({email})")