# Pizza Toppings: Write a loop that prompts the user to enter a series of pizza toppings until they
# enter a 'quit' value. As they enter each topping, print a message saying you'll add that topping to their pizza.

# TO ENTER THE WHILE LOOP I'VE ASSIGNED AN INITIAL VALUE TO THE VARIABLE TOPPING AS AN EMPTY STRING OTHERWISE
# THE PROGRAM WON'T RUN. 

# THE INITIAL VALUE STARTS THE LOOP WHEREBY AN INPUT WILL ASK USERS FOR A TOPPING AS A RESPONSE. THE CONDITION IS MET 
# WHEN ANY STRING APART FROM 'QUIT' IS A RESPONSE WHICH IS THEN APPENDED TO A LIST. THE LIST IS INITIALLY EMPTY.
# IN THE PROCESS THE SECOND CONDITION VIA THE IF STATEMENT IS ALSO MET IN THE EVENT THE RESPONSE IS NOT 'QUIT'.
# AS TOPPINGS ARE ADDED TO THE LIST, A FOR LOOP IS USED TO PRINT EACH VALUE.
# UPON 'QUIT' BEING ENTERED AS A RESPONSE, LOOP IS EXITED - ENDING THE PROGRAMMING.

topping = ""

toppings = []

while topping != 'quit':
    topping = input("What toppings would you like on your pizza? When finished enter 'quit'. ")
    toppings.append(topping)

    if topping != 'quit':
        print('THE PIZZA MASTERPIECE WITH THE FOLLOWING TOPPINGS:')
        for ingredient in toppings:
            print(ingredient)



   



