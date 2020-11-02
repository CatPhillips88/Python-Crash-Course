# Favourite Numbers: Modify your program from Exercise 6.2 so each person can have more than one favourite number.
# Then each person's nasme along with their favourite numbers.

favourite_numbers = {
  'jennifer': [12, 100],
  'cat': [10, 3],
  'derek': [26, 16, 88],
  'sharon': [45, 7853],
  'lilly': [11, 3333]
}

for person, number in favourite_numbers.items():
  print(f'\n{person.title()}\'s favourite number/s:')
  for favourite in number:
    print(f'{favourite}')
 

# Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary.
# Create a dictionary of information about each city and include the country that the city is in, its approximate population,
# and one fact about that city.
# The keys for each city's dictionary should be something like country, population and fact. Print the name of each city
# and all of the information you have stored about it.

cities = {
   'los angeles': {
     'country': 'north america',
     'population': 3.99,
     'fact': 'When LA was founded, the city\'s full name was El Pueblo de Nuestra Senora Reina de los Angeles sobre el Rio Porciuncula in Spanish \nwhich translates to The town of our lady queen of the angels on the Porciuncula River.' 
   },
   'berlin': {
     'country': 'germany',
     'population': 3.64,
     'fact': 'Napoleon stole Quadriga statue (the goddess on a chariot drawn by four horses) on top of the Brandenburg Gate \nwhen the city was captured by French forces in 1806 during the Fall of Berlin.'

   },
   'montego bay': {
     'country': 'jamaica',
     'population': 427,
     'fact': 'Have you ever heard about the haunted The Rose Hall Great House?\nIt is the house of the widowed Annie Mary Patterson who murdered all her 3 husbands and practiced voodoo.'
   }
}

for city, city_info in cities.items():
  print(f'\n{city.title()}')

  country = f'Country: {city_info["country"].title()}'
  print(country)

  if city_info["population"] == 427:
    print(f'Population: {city_info["population"]} thousand')
  else:
    print(f'Population: {city_info["population"]} million')

  fact = f'Fun Fact: {city_info["fact"]}'
  print(fact)





