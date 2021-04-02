# T-shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# The function should print a sentence summarising the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.

def make_shirt(size, message):
    print(f'Shirt Size: {size.upper()}')
    print(f'Message: {message}')

make_shirt('xs', 'It\'s my birthday and all I got was this T-shirt')
make_shirt(message='Don\'t be vague. Ask for a T-shirt', size='m')

# Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads 'I love Python'. 
# Make a large shirt and medium shiirt with the default message, and a shirt size of any size with a different message.

def make_shirt(size= 'l', message= 'I love Python'):
    print(f'Shirt Size: {size.upper()}')
    print(f'Message: {message}')

make_shirt()
make_shirt('m')
make_shirt(message= 'Python-Lickin Good!', size='s')

# Cities: Write a functiion called describe_city() that accepts the name of a city and its country. The functions should print
# a simple sentence such as 'Rekjavik is in Iceland'. Give the parameter for the country a default value. Call your function
# for three different cities, at least one of which is not in the default country.

def describe_city(city, country= 'United Kingdom'):
    print(f'{city.title()} is in {country.title()}')

describe_city(city= 'asuncion', country= 'paraguay')
describe_city('castries', 'st lucia')
describe_city(country= 'south africa', city= 'johannesburg')
