# People: Start with the program you wrote for Persons. Make two new dictionaries representing different people, and store all
# three dictionaries in a list called people. Loop through your list of people. As you loop through the list, print everything
# you know about each person.

person1 = {
    'first_name': 'jennifer',
    'last_name': 'oliver',
    'age' : 58,
    'city': 'kent'
}

person2 = {
    'first_name': 'carlton',
    'last_name': 'allison',
    'age' : 30,
    'city': 'london'
}

people = [person1, person2]



for person in people:
    print(f'\n{person["first_name"].title()}\'s profile:')
   
    full_name = f'\tFull name: {person["first_name"].title()} {person["last_name"]}'
    age = f'\tAge: {person["age"]}'
    city = f'\tCity: {person["city"]}'
        
    print(full_name)
    print(age)
    print(city)

    
        
        