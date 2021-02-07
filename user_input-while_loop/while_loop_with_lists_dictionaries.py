# Deli: Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called
# finished_sandwiches. Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwch.
# As each sandwich is made, move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listiing
# each sandwich that was made.

sandwich_orders = ['grilled cheese', 'pulled pork', 'club', 'bacon', 'french dip']

finished_sandwiches = []

while sandwich_orders:
    order = sandwich_orders.pop()
    print(f'You\'re {order.title()} sandwich is currently being made')
    finished_sandwiches.append(order)


for sandwich_made in finished_sandwiches:
    print(f'I made your {sandwich_made.title()} sandwich')

print('\nLIST OF FINISHED SANDWICHES')
for sandwich in finished_sandwiches:
    print(sandwich.title())

