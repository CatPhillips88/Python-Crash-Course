# Exercises

# Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive

for value in range(1, 21):
    print(value)


# Summing a Million: Make a list of the numbers from one to one million, and then use min() and max()
# to make sure your list actually starts from one and ends at one million. Also use the sum() function to see how 
# quickly Python can add a million numbers.

million = list(range(1, 1000001))

print(min(million))

print(max(million))

print(sum(million))


# Odd Numbers: Use the third argument of the range() function to make a list of a list of the odd numbers from 1 to 20.
# Use a for loop to print each number.

odd_numbers = list(range(1, 21, 2))

for number in odd_numbers:
    print(number)


# Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list.

threes = list(range(3, 31, 3))

for number in threes:
    print(number)


# Cubes: A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python
# Make a list of the first 10 cubes(that is, the cube of each integer from 1 through 10), and use a for loop to print
# out the value of each cube

cubes = []

for cube in range(1, 11):
    value = cube**3
    cubes.append(value)
    print(value)


# Cube Comprehension: Use list comprehension to generate a list of the first 10 cubes

cubes = [cube**3 for cube in range(1, 11)]

print(cubes)


   



