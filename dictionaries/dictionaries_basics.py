# Exercises

# Persons: Use a dictionary to store information about a person you know. Store their first name, 
# last name, and the city which they live. You should have keys such as first_name, last_name, age
# and city. Print each piece of information stored in your dictionary.

person = {
    'first_name': 'Jennifer',
    'last_name': 'Oliver',
    'age' : 58,
    'city': 'Kent'
}

print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

# Favourite Numbers: Use a dictionary to store people's favourite numbers. Think of five names, and 
# use them as keys in your dictionary. Think of a favourite number for each person, and store each 
# as a value in your dictionary. Print each person's name and their favourite number.

favourite_numbers = {
    'Jennifer': 12,
    'Cat': 3,
    'Derek': 4,
    'Sharon': 10,
    'Lilly': 11
}

print(f'Jen\'s favourite number: {favourite_numbers["Jennifer"]}')

print(f'Cat\'s favourite number: {favourite_numbers["Cat"]}')

print(f'Derek\'s favourite number: {favourite_numbers["Derek"]}')

print(f'Sharon\'s favourite number: {favourite_numbers["Sharon"]}')

print(f'Lilly\'s favourite number: {favourite_numbers["Lilly"]}')


# Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion
# let's call it a glossary.

# Think of five programming words you've learned about in the previous chapters. Use these words as keys
# in your glossary, and store their meanings as values.

# Print each word and its meaning as neatly formatted output. You might print the word followed by a colon
# and then its meaning, or print the word on one line and then print its meaning indented on a second liine.
# Use the newline characted \n to insert a blank line between each word-meaning pair in your output.

programming_glossary =  {
    'Loop': 'Where you can perform a task for values for example in a list, tuple or dictionary',
    'Tuple': 'A list that essentially cannot be modified',
    'List': 'A collection of items in a particular order',
    'If Statement': 'A condition that allows you perform an action depending boolean value being executed',
    'List Comprehension': 'Refactoring code block into one line. Often seen in lists'
}


print(f'\nLoop: {programming_glossary["Loop"]}\n')

print(f'Tuple: {programming_glossary["Tuple"]}\n')

print(f'List: {programming_glossary["List"]}\n')

print(f'If Statement: {programming_glossary["If Statement"]}\n')

print(f'List Comprehension: {programming_glossary["List Comprehension"]}\n')