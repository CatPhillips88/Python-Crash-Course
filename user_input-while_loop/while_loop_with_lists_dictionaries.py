# Deli: Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called
# finished_sandwiches. Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwch.
# As each sandwich is made, move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listiing
# each sandwich that was made.

sandwich_orders = ['grilled cheese', 'pulled pork', 'club', 'bacon', 'french dip']

finished_sandwiches = []

while sandwich_orders:
    order = sandwich_orders.pop()
    print(f'Your {order.title()} sandwich is currently being made')
    finished_sandwiches.append(order)


for sandwich_made in finished_sandwiches:
    print(f'I made your {sandwich_made.title()} sandwich')

print('\nLIST OF FINISHED SANDWICHES')
for sandwich in finished_sandwiches:
    print(sandwich.title())

# No Pastrami: Using the list sandwich_orders, make sure the sandwich 'pastrami' appears in the list at least three tiimes. Add code near the
# beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurences of 
# 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.

sandwich_orders = ['pastrami', 'grilled cheese', 'pulled pork', 'pastrami', 'club', 'bacon', 'french dip', 'pastrami']

finished_sandwiches = []

print('THE DELI HAS RUN OUT OF PASTRAMI SANDWICHES')

while 'pastrami' in sandwich_orders:
    remove_sandwich = sandwich_orders.remove('pastrami')

while sandwich_orders:
    order = sandwich_orders.pop()
    print(f'Your {order.title()} sandwich is currently being made')
    finished_sandwiches.append(order)


for sandwich_made in finished_sandwiches:
    print(f'I made your {sandwich_made.title()} sandwich')

print('\nLIST OF FINISHED SANDWICHES')
for sandwich in finished_sandwiches:
    print(sandwich.title())



