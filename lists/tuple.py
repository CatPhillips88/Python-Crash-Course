# Exercises

# Buffet: A buffet-style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.

# Use a for loop to print each food the restaurant offers.

# Try to modify one of the items, and make sure that Python rejects the change.

# The restaurant changes its menu, replacing two of the items with different foods. Add a new line that rewrites the tuple,
# and then use a for loop to print each of the items on the revised menu

buffet_food = ('mac & cheese', 'roast chicken', 'wong tong soup', 'gua bao', 'pepper soup')

buffet_food = ('jerk chicken', 'beef korma', 'wong tong soup', 'gua boa', 'pepper soup')

for food in buffet_food:
  print(food.title())
