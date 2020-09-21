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

 