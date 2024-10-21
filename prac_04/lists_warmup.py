numbers = ["ten", 1, 4, 1, 5, 9, 1]
numbers[0] # ans: 3
numbers[-1] # ans: 2
numbers[3] # ans: 1
numbers[:-1] # ans: [3, 1, 4, 1, 5, 9]
numbers[3:4] # ans: [3,5]
5 in numbers # ans: True
7 in numbers # ans: False
"3" in numbers # ans: False
numbers + [6, 5, 3] # ans: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
# Part 3
slice_first_two_numbers = slice(2, 7)
print(numbers[slice_first_two_numbers])
# Part 4
print(9 in numbers)