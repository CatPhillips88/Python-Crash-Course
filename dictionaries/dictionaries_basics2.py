# Glossary 2: Clean up the code from the previous exercise "Glossary" by replacing your series of print()
# calls with a loop that runs through the dictionary's keys and values. 
# When you're sure that your loop works, add five more Python terms to your glossary. When you run your
# program again, these new words and meanings should automatically be included in the output.


programming_glossary =  {
    'loop': 'Where you can perform a task for values for example in a list, tuple or dictionary',
    'tuple': 'A list that essentially cannot be modified',
    'list': 'A collection of items in a particular order',
    'append': 'A method to add elements to lists',
    'if statement': 'A condition that allows you perform an action depending boolean value being executed',
    'list comprehension': 'Refactoring code block into one line. Often seen in lists',
    'dictionary': 'A collection that contains a series of key-value pairs',
    'key-value pairs': 'A set of values connected to each other',
    'comment': 'Represented by the # symbol - Programmers use this to explain a how specific code block works',
    'range': 'A numerical function used to generate a series of numbers within a defined range'
}

for term, description in programming_glossary.items():
    print(f'{term.title()} - {description}')

# Rivers: Make a dictionary containing three major rivers and the country each river runs through. 

# Use a loop to print a sentence about each river, such as The Nile runs through Egypt

# Use a loop to print the name of each river included in the dictionary.

# Use a loop to print the name of each country included in the dictionary.

rivers = {
    'nile': 'africa',
    'amazon': 'south america',
    'yangtze': 'china'
}

for river, country in rivers.items():
    if river == 'nile':
        print(f'The {river.title()} in {country.title()} is the longest river in the world')
    elif river == 'amazon':
        print(f'The {river.title()} in {country.title()} is the second longest river in the world')
    elif river == 'yangtze':
        print(f'The {river.title()} in {country.title()} is the third longest river in the world')

for river in rivers.keys():
    print(river.title())

for river in rivers.values():
    print(river.title())


# Polling: Use previous code from favourite programming languages (within book) -

# Make a list of people who should take the favourite languages poll. Include some names that are
# already in the dictionary and some that are not.

# Loop through the list who should take the poll. If they have already taken the poll, print a message
# thanking them for responding.
# If they have not yet taken the poll, print a messgae inviting them to take the poll.

favourite_languages = {
    'jon': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'shona': 'scala'
}

people = ['edward', 'shona', 'pia', 'mario']

for person in favourite_languages.keys():
    if person in people:
        print(f'{person.title()}, thank you for taking the poll!')
    else:
        print(f'{person.title()}, please take the poll')