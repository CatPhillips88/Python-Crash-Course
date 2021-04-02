# Pizza Toppings: Write a loop that prompts the user to enter a series of pizza toppings until they
# enter a 'quit' value. As they enter each topping, print a message saying you'll add that topping to their pizza.

# TO ENTER THE WHILE LOOP I'VE ASSIGNED AN INITIAL VALUE TO THE VARIABLE TOPPING AS AN EMPTY STRING OTHERWISE
# THE PROGRAM WON'T RUN. 

# THE INITIAL VALUE STARTS THE LOOP WHEREBY AN INPUT WILL ASK USERS FOR A TOPPING AS A RESPONSE. THE CONDITION IS MET 
# WHEN ANY STRING APART FROM 'QUIT' IS A RESPONSE WHICH IS THEN APPENDED TO A LIST. THE LIST IS INITIALLY EMPTY.
# IN THE PROCESS, THE SECOND CONDITION VIA THE IF STATEMENT IS ALSO MET IN THE EVENT THE RESPONSE IS NOT 'QUIT'.
# AS TOPPINGS ARE ADDED TO THE LIST, A FOR LOOP IS USED TO PRINT EACH VALUE.
# UPON 'QUIT' BEING ENTERED AS A RESPONSE, LOOP IS EXITED - ENDING THE PROGRAM.

topping = ""

toppings = []

while topping != 'quit':
    topping = input("What toppings would you like on your pizza? When finished enter 'quit'. ")
    toppings.append(topping) 

    if topping != 'quit':
        print('YOUR PIZZA MASTERPIECE WITH THE FOLLOWING TOPPINGS:')
        for ingredient in toppings:
            print(ingredient)


# Movie Tickets: A movie theater charges different ticket prices depending on a person's age. If a person is under the age of 3,
# the ticket is free. If they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop
# in which you ask users their age, and then tell them the cost of their movie ticket.

while True:
    age = int(input('How old are you? '))
    if age < 3:
        print('Movie tickets are free')
        break
    elif age < 12:
        print('Movie tickets are $10')
        break
    elif age > 12:
        print('Movie tickets are $15')
        break


# Three Exits: Write different versions of the Pizza Toppings exercise that do each of the following at least once:
# Use a conditional test in the while statement to stop the loop
# Use an active variable to control how long the loop runs
# Use a break statement to exit the loop when the user enters a 'quit' value

# EXAMPLE ONE

topping = ''
toppings = []

active = True

while len(toppings) < 5:
    topping = input('What toppings would you like on your pizza? ')
    toppings.append(topping)

    print('\nYOUR PIZZA  MASTERPIECE INCLUDES THE FOLLOWING TOPPINGS:')

    for ingredient in toppings:
        print(ingredient)

# EXAMPLE TWO

while active:
    topping = input('What toppings would you like on your pizza? ')
    toppings.append(topping)

    if len(toppings) == 5:
        print('\nYOUR PIZZA  MASTERPIECE INCLUDES THE FOLLOWING TOPPINGS:')

        for ingredient in toppings:
            print(ingredient)
        active = False

# EXAMPLE THREE
# IF STATEMENT USED WITHIN FOR LOOP TO REMOVE THE VALUE 'quit' FROM THE LIST.

while True:
    topping = input('What toppings would you like on yur pizza? Enter "quit" when you have finished. ')
    toppings.append(topping)

    if topping == 'quit':
        print('\nYOUR PIZZA  MASTERPIECE INCLUDES THE FOLLOWING TOPPINGS:')
        for ingredient in toppings:
            if ingredient == 'quit':
                toppings.remove('quit')
            else:
                print(ingredient)
        break
