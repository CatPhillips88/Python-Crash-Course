# Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. The function should have one
# that collects as many items as the function call provides, and it should print a summary of the sandwich that's being ordered.
# Call the function three times, using a different number of arguments each time.

def sandwich_order(*fillings):
    print('YOUR SANDWICH CONTAINS THE FOLLOWING FILLINGS:')
    for filling in fillings:
        print(filling.title())

sandwich_order('tomato', 'red leicester cheese', 'mayo')
sandwich_order('chicken', 'cranberry sauce')
sandwich_order('veggie sausage', 'red pepper', 'hummus')

# User Profile: Start with a copy of user_profile.py. Build a profile of yourself by calling build_profile(), using your first
# and last names and three other key-value pairs that describe you.

def user_profile(first, last, **profile):
    profile['first name'] = first
    profile['last name'] = last
    return profile

add_personal_data = user_profile('catherine', 'phillips', age = 33, location='beckenham')
print(add_personal_data)

# Cars: Write a function that stores information about a car in a dictionary. The function should always receive a manufaturer and a model name.
# It shuld then accept an arbitrary number of keyword arguments. Call the function with the required information and two other name-value pairs, 
# such as a colour or an optional feature. Your function should work for a call like this one: car = make_car('subaru', 'outback', color='blue, tow_package=True).
# Print the dictionary that's returned to make sure all information was stored correctly.

def make_car(manufacturer, model_name, **car_features):
    car_features['make'] = manufacturer
    car_features['model'] = model_name
    return car_features

add_car_features = make_car('mercedes', 'g-class', colour='china blue', wheels='20" alloy', finish='high-sheen')
print(add_car_features)
