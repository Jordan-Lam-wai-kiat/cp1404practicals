#Qn1
name = input("Enter your name: ")
open_file = open("name.txt", "w")
print(name, file=open_file)
open_file.close()

#Qn2
open_file = open("name.txt", "r")
print("hi", open_file.readline())

#Qn3
with open("numbers.txt", "r") as open_file:
    contents = open_file.readlines()
total = int(contents[0]) + int(contents[1])
print(total)

#Qn4
total = 0
with open("numbers.txt", "r") as open_file:
    for line in open_file:
        total += int(line)
print(total)