"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    display_subject_details(data)

def display_subject_details(data):
    """displays subject details for each person inside the nested list, line for line."""
    for nested_list in data:
        print(f"{nested_list[0]} is taught by {nested_list[1] :12} and has {nested_list[2] :3} students")

def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    compiled_list_of_credentials = []
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        compiled_list_of_credentials.append(parts)
        print(compiled_list_of_credentials)
        print("----------")
    input_file.close()
    return compiled_list_of_credentials

main()