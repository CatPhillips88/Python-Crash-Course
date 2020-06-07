# Exercises

# Dinner Guests: Working with one of the programs from the dinner guest exercise, use len() to print a message indicating
# the number of people you are inviting to dinner.

guest_list =  ['Rihanna', 'Steve Jobs', 'Bernardine Evaristo', 'Gucci Mane', 'Gabriel Garcia Marquez']

guest_list.insert(3, 'Robert Greene')

guest_list.insert(0, 'Norman Manley')

guest_list.insert(2, 'Tariq Nasheed')

guest_list.append('Vybz Kartel')

how_many_invited = len(guest_list)

print(f"There are {how_many_invited} guests invited to dinner")
