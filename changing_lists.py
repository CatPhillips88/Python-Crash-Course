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

print('Hey all, I\'ve found a new place to hold our cookout! It\'s much bigger!!')

guest_list.insert(0, 'Norman Manley')

guest_list.insert(2, 'Tariq Nasheed')

guest_list.append('Vybz Kartel')

print(f"You're invite to the cookout, {guest_list[0]}!")

print(f"You're invite to the cookout, {guest_list[1]}!")

print(f"You're invite to the cookout, {guest_list[2]}!")

print(f"You're invite to the cookout, {guest_list[3]}!")

print(f"You're invite to the cookout, {guest_list[4]}!")

print(f"You're invite to the cookout, {guest_list[5]}!")

print(f"You're invite to the cookout, {guest_list[6]}!")

print(f"You're invite to the cookout, {guest_list[7]}!")








