# Message: Write a function called display_message() that prints one sentence telling everyone what you are 
# learning about this chapter. Call the function, and make sure the message displays correctly.

def display_message():
    print('Function are named blocks of code designed to do one specific.')
display_message()

# Favourite Book: Write a function called favourite_book() that accepts one parameter, title. The function should
# print a message, such as One of my favourite books is Alice in Wonderland. Call the function, making sure to include
# a book title as an argument in the function call.

def favourite_book(title):
    print(f'One of my favourite books is {title.title()}')
favourite_book('soul tourists')