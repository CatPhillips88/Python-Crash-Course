# Exercises

# Write a series of conditions tests that run both True & False boolean results for the following:

# EQUALITY & INEQUALITY WITH STRINGS

milkshake = 'Banana'

# print(milkshake == 'Banana')
  
# print(milkshake != 'Oreo')
   
# print(milkshake == 'Strawberry')

# print(milkshake != 'Banana')

# USING THE LOWER() METHOD

bridge = 'Tower Bridge'

# print(bridge.lower() == 'tower bridge')
 
# print(bridge.lower() == 'TOWER BRIDGE')
 
# NUMERICAL TESTS - EQUALITY & INEQUALITY, GREATER THAN AND LESS THAN, GREATER THAN OR EQUAL TO, LESS THAN OR EQUAL TO

print(456 == 456)

print(6981 != 76)

print(12 == 200000)

print(32 != 32)

print(131261 > 12987)

print (2 < 90)

print(401 > 555)

print(810 < 809)

print (2.6756 >= 1.45)

print(765.88 >= 885.67)

print(50 <= 123)

print(702 <= 1)

# TESTS USING THE 'AND' KEYWORD & 'OR' KEYWORD

age_entry = 20
 
if age_entry >= 18 and age_entry <= 25:
   print(f'YOU MAY ENTER THE COMPETITION')


age_entry2 = 16

if age_entry2 >= 18 and age_entry2 <= 25:
   print(f'YOU MAY ENTER THE COMPETITION')


user1 = 'cITrine0654'   
user2 = 'AMethYST327'

if (user1 == 'cITrine0654') or (user2 == 'TouRMALine1245'):
    print(f'ACCESS GRANTED')
else:
	print(f'ACCESS DENIED')


if (user1 == 'QuArtZ129') or (user2 == 'TouRMALine1245'):
	print(f'ACCESS GRANTED')
else:
	print(f'ACCESS DENIED')

# TEST WHETHER ITEM IS IN A LIST

Jamaican_Flag = ['Black', 'Green', 'Gold']

if 'Gold' in Jamaican_Flag:
    print('WAVE YOUR FLAG!')

# TEST WHETHER ITEM IS NOT IN A LIST

German_Flag = ['Black', 'Red', 'Yellow']

if 'Blue' not in German_Flag:
    print('YOU HAVE THE WRONG FLAG!')

