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

# Pets: Create a few dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal 
# and the owner's name. Store the dictionaries in a list called pets. Next, loop through your list and as you do, print everything
# you know about each pet.

cat = {'breed': 'british shorthair', 'animal': 'cat', 'owner': 'quentin'}

dog = {'breed': 'boston terrier', 'animal': 'dog', 'owner': 'kate'}

iguana = {'breed': 'green', 'animal': 'iguana', 'owner': 'sam'}

turtle = {'breed': 'red eared slider', 'animal': 'turtle', 'owner': 'arizona'}

pets = [cat, dog, iguana, turtle]

for pet in pets:
    print(f'\n{pet["owner"].title()} has a {pet["breed"].title()} {pet["animal"]}')


# Favourite Places:  Make a dictionary called favourite_places. Think of three names to use as keys in the dictionary,
# and store one to three favourite places for each person. To make this exercise a bit more interestng,
# ask some friends to name a few of their favourite places. Loop through the dictionary, and print
# each person's name and their favourite places.

favourite_places = {
  'maria': 'st pauls cathedral',
  'richard': 'up at the o2',
  'zara': 'sky garden'
}

for person, place in favourite_places.items():
  print(f'{person.title()}\'s favourite place: {place.title()}')