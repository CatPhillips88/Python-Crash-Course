# Exercises

# Slices: Create a program and add lines that do the following:

# Print the message 'The first three items in the list are:'. Then use a slice to print
# the first three items from that program's list

# Print the message 'Three items from the middle of list are:'. Use a slice to print
# three items from the middle of the list.

# Print the message 'The last three items in the last are:'. Use a slice to print the last 
# three items in the list

favourite_games = ['mario kart', 'mortal kombat', 'GTA vice city', 'need for speed', 'la noire']

# for game in favourite_games[:3]:
#     print(game.title())

# for game in favourite_games[1:4]:
#     print(game.title())

# for game in favourite_games[-3:]:
#     print(game.title())



# My Pizzas, Your Pizzas: Create a program and make a copy of a list of pizzas, and call
# it friend_pizzas. Then do the following:

# Add a new pizza to the original list
# Add a different pizza to the list friend_pizza.

# Prove that you have two separate lists. Print the message 'My favourite pizzas are:' and use a for loop to
# print the first list.

# Print the message 'My friend's favourite pizzas are:' and then use a for loop to print the second list. 
# Make sure each new pizza is stored in the appropriate list.

my_pizzas = ['pepperoni', 'hawaiian', 'califonian', 'chicago', 'neapolitan']

friends_pizza = my_pizzas[:]

my_pizzas.append('veggie')

friends_pizza.append('buffalo')



print(f'My favourite pizzas are:')
for pizza in my_pizzas:
    print(pizza.title())

print(f'\nMy friend\'s favourite pizzas are:')
for pizza in friends_pizza:
    print(pizza.title())
