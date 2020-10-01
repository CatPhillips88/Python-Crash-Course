# Exercises

# Hello Admin: Make a list of five or more usernames, including the name 'admin'. Imagine you are writing
# code that will print a greeting to each user after they log in to a website. Loop through the list, and
# print a greeting to each user:

# If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status
# report?

# Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging in again

usernames = ['michelle', 'romain', 'admin', 'dave', 'lola']

for username in usernames:
    if username == 'admin':
        print('Hello admin, would you like to see a status report?')
    else:
        print(f'Hello {username.title()}, thanks your for logging in again')


# No Users: Add an if test to hello admin to make sure the list of users is not empty.

# If the list is empty, print the message We need to find some users!

# Remove all of the usernames from your list, and make sure the correct message is printed.

usernames2 = []

if usernames2:
    print('We have some users')
else:
    print('We need to find some users!')


# Checking Usernames: Do the following to create a program that stimulates how websites ensure that everyone has 
# a unique username.

# Make a list of five or more usernames called current_users

# Make another list of five usernames called new_users. Make sure one or two of the new usernames are also in
# the current_users list

# Loop through the new_users list to see if each new username has already been used. If it has, print a message
# that the person will need to enter a new username. If a username has not been used, print a message saying
# that the username is available.

# Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted. (To do
# this, you'll need to make a copy of current_users containing the lowercase versions of all existng users.)


# PSUEDOCODE: a for loop is used to append values found in current_users to a formatted case value in current_users2
# Then another loop reads each value of new_users list where a check to see whether new_user value can
# be found in the current_users2 list.
# The new_user value has a condition set to lower case to match lower casing values in current_users2. 
# If values from both lists match then users will be asked to submit another username


current_users = ['mabel', 'christian', 'lisa', 'arnold', 'jodie', 'John']
new_users = ['arnold', 'tim', 'rosaline', 'christian', 'maria', 'JOHN']

current_users2 = []

for user in current_users:
    current_users2.append(user.lower())

for new_user in new_users:
    if new_user.lower() in current_users2:
        print(f'Username: {new_user} is not available, please choose another')
    else:
        print(f'Username: {new_user} is available')


# Ordinal Numbers: Ordinal numbers indicate their position in a list such as 1st or 2nd. Most ordinal numbers
# end in th, except 1, 2 and 3

# Store the numbers 1 through 9 

# Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number. Your output should
# read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line.

ordinal_number = list(range(1, 10))

for num in ordinal_number:
  if num == 1:
    print(f'{num}st')
  elif num == 2:
    print(f'{num}nd')
  elif num == 3:
    print(f'{num}rd')
  else:
    print(f'{num}th')
