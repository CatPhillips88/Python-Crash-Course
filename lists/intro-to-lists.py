# Exercises

# Names: Store the names of a few of your friends in a list called names. Print each person's
# name by accessing each element in the list, one at a time.

names = ['Arnold', 'Lola', 'Zara', 'Carlton']

print(names[0])

print(names[1])

print(names[2])

print(names[3])


# Greetings: Start with the list you used before, but instead of just print each person's name
# print a message to them. The text of each message should be the same, but each message should
# be personalised with the person's name.

print(f"How are you, {names[0]}?")

print(f"How are you, {names[1]}?") 

print(f"How are you, {names[2]}?") 

print(f"How are you, {names[3]}?") 


# Your Own List: Think of your favourite mode of transportation, such as a motocycle or a car, and
# make a list that stores a number of examples. Use your list to print a series of statements about these
# items, such as  "I would like to own a Honda motocycle."

cars = ['g-Wagon', 'range rover', 'aventador', 'tesla']

choice = f"I would like to own a"

print(f"{choice} {cars[0].title()}")

print(f"{choice} {cars[1].title()}")

print(f"{choice} {cars[2].title()}")

print(f"{choice} {cars[3].title()}")