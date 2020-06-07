# Exercises

# Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes 
# at least three people you'd like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.

guest_list =  ['Rihanna', 'Steve Jobs', 'Bernardine Evaristo', 'Gucci Mane', 'Gabriel Garcia Marquez']

# print(f"You're invite to the cookout, {guest_list[0]}!")

# print(f"You're invite to the cookout, {guest_list[1]}!")

# print(f"You're invite to the cookout, {guest_list[2]}!")

# print(f"You're invite to the cookout, {guest_list[3]}!")

# print(f"You're invite to the cookout, {guest_list[4]}!")



# Changing Guest List: You just heard that one of your guests can't make the dinner, so you need to send out a new set of 
# invitations. You'll have to think of someone else to invite.

# Start with your program from the previous exercise. Add a print() call at the end of your program stating the name of
# the guest who can't make it.

# Modify your list, replacing the name of the guest who can't make it with the name of the new person you are inviting.

# Print a second set of invitation messages, one for each person who is still in your list.

cancelled_guest = 'Gucci Mane'
guest_list.remove(cancelled_guest)

print(f"Unfortunately {cancelled_guest} cannot make it! You'll be missed!")

guest_list.insert(3, 'Robert Greene')

# print(f"You're invite to the cookout, {guest_list[0]}!")

# print(f"You're invite to the cookout, {guest_list[1]}!")

# print(f"You're invite to the cookout, {guest_list[2]}!")

# print(f"You're invite to the cookout, {guest_list[3]}!")

# print(f"You're invite to the cookout, {guest_list[4]}!")



# More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests 
# to invite to dinner.

# Start with either previous programs. Add a print() call to the end of your program informing people that you
# found a bigger table.
 
# Use insert() to add one new guest to the beginning of your list

# Use insert() to add one new guest to the middle of your list.

# Use append() to add one new guest to the end of your list.

# Print a new set of invitation messages, one for each person in your list.

# print('Hey all, I\'ve found a new place to hold our cookout! It\'s much bigger!!')

guest_list.insert(0, 'Norman Manley')

guest_list.insert(2, 'Tariq Nasheed')

guest_list.append('Vybz Kartel')

# print(f"You're invite to the cookout, {guest_list[0]}!")

# print(f"You're invite to the cookout, {guest_list[1]}!")

# print(f"You're invite to the cookout, {guest_list[2]}!")

# print(f"You're invite to the cookout, {guest_list[3]}!")

# print(f"You're invite to the cookout, {guest_list[4]}!")

# print(f"You're invite to the cookout, {guest_list[5]}!")

# print(f"You're invite to the cookout, {guest_list[6]}!")

# print(f"You're invite to the cookout, {guest_list[7]}!")


# Shrinking Guest List: You just found out that your new dinner table won't arrive in time for the dinner,
# and you have space for only two guests.

# Start with your program from the previous exercise. Add a new line that prints a message saying that you
# can invite only two people for dinner.

# Use pop() to remove guests from your list one at a time until only two names remain in your list. 
# Each time you pop a name from your list, print a message to that person letting them know you're sorry 
# you can't invite them to dinner.

# Print a message to each of the two people still on your list, letting them know they're still invited.

# Use del to remove the last two names from your list, so you have an empty list. Print your list to
# make sure you actually have an empty list at the end of your program.

print(f"Really sorry everyone, unfortunately my dinner table hasn't come so I can only invite 2 guests now...") 

cancelled_message = f"I'm sorry I have to uninvite you, "

cancelled_guest1 = guest_list.pop(-1)
cancelled_guest2 = guest_list.pop(-2)
cancelled_guest3 = guest_list.pop(-3)
cancelled_guest4 = guest_list.pop(-4)
cancelled_guest5 = guest_list.pop(3)
cancelled_guest6 = guest_list.pop(2)

print(cancelled_message + cancelled_guest1)

print(cancelled_message + cancelled_guest2)

print(cancelled_message + cancelled_guest3)

print(cancelled_message + cancelled_guest4)

print(cancelled_message + cancelled_guest5)

print(cancelled_message + cancelled_guest6)

# start at index 0 to delete list elements
del guest_list[0:]  

print(guest_list)






