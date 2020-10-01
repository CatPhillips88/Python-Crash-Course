# Alien Colors #3: Turn your if-else chain into an if-elif-else chain.

# If the alien is green, print a message that the player earned 5 points.

# If the alien is yellow, print a message that the player earned 10 points.

# If the alien is red, print a message that the player earned 15 points.

alien_color =  'yellow'

if alien_color == 'green':
    print('Player 1 has earned 5 points')
elif alien_color == 'yellow':
    print('Player 1 has earned 10 points')
else:
    print('Player 1 has earned 15 points')


# Stages of Life: Write an if-elif-else chain that determines a person's stage of life. Set a value for the variable age, and then:

# If a person is less than 2 years old, print a message that the person is a baby

# If the person is at least 2 years old but less than 4, print a message that the person is a toddler.

# If the person is at least 4 years old but less than 13, print a messgae that the person is a kid.

# If the person is at least 13 years old but less than 20, print a message that the person is a teenager

# If the person is at least 20 years old but less than 65, print a message that the person is an an adult

# If the person is at least 65 or older, print a message that the person is an elder

age = 16

if age < 2:
    print('You\'re a baby')
elif age >= 2 and age < 4:
    print('You\'re a toddler')
elif age >= 4 and age < 13:
    print('You\'re a kid')
elif age >= 13 and age < 20:
    print('You\'re a teenager')
elif age >= 20 and age < 65:
    print('You\'re an adult')
else:
    print('You\'re an elder')


# Favourite Fruit: Make a list of your favourite fruits, and then write a series of independent if statements that check for 
# certain fruits in your list.

# Make a list of your three favourite fruits and call it favourite_fruits

# Write five if statements. Each should check whether a certain kind of fruit is in your list. If the fruit is your list, the
# if code block should print a statement, such as You really like bananas!

favourite_fruits = ['Apples', 'Grapes', 'Oranges']

if 'Oranges' in favourite_fruits:
    print('You really like oranges!')

if 'Kiwi' in favourite_fruits:
    print('You really like kiwi!')

if 'Pineapples' in favourite_fruits:
    print('You really like pineapples!')

if 'Grapes' in favourite_fruits:
    print('You really like grapes!')

if 'Apples' in favourite_fruits:
    print('You really like apples!')