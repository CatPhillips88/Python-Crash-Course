# Exercises

# Personal Message: Use a variable to represent a person's name, and print a message to that person. 
# Your message should be simple, such as, "Hello Eric, would you like to learn Python today?"

name = "Cat"

print(f"Hello {name}, would you like to learn Python today?")

# Name Cases: Use a variable to represent a person's name, and then print that person's name in 
# lowercase, uppercase, and title case.

name = "jennifer oliver"

print(f"{name.lower()}")
print(f"{name.upper()}")
print(f"{name.title()}")

# Famous Quote: Find a quote from a famous person you admire. Print the quote and the name of its author. 
# Your output should look something like the following, including the quotation marks:
# Albert Einstein once said, "A person  who never made a mistake never tried anything new."

quote = "Infection: Avoid the unhappy or the unlucky"

author = "robert greene"

print(f'{author.title()} once said, "{quote}".')

# Famous Quote 2: Repeat the previous exercise, but this time represent the famous person's name using
# a variable called famous_person. Then compose your message and represent it with a new variable called message. 
# Print your message

famous_person = "robert greene"

message = f'{famous_person.title()}, once said "Infection: Avoid the unhappy or the unlucky".'

print(message)

# Stripping Names: Use a variable to represent a person's name, and include some whitespace characters at the beginning,
# and end of the name. Make sure you use each character combination, "\t" and "\n", at least once.
# Print the name once, so the whitespace around the name is display. Then print the name using each of the three stripping
# functions, lstrip(), rstrip() and strip()

who_are_you = "\tCatherine\n\t "

print(who_are_you)

print(who_are_you.lstrip())

print(who_are_you.rstrip())

print(who_are_you.strip())




