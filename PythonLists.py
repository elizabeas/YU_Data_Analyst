# Create three lists: a grocery list that includes milk, eggs, bread, and jam; a list of items already in the pantry and refrigerator 
# that includes almonds, macaroni, coffee, and bacon; and also a blank list for "maybe need" items.
# Print the contents of each list to confirm what has been added.
grocery_list = ['milk', 'eggs', 'bread', 'jam']
pantry_fridge = ['almonds', 'macaroni', 'coffee', 'bacon']
maybe_need_list = []
print(grocery_list)
print(pantry_fridge)
print(maybe_need_list)


# Create an input variable to ask what additional item might be added to the grocery list
new_item = input("What other item might need to be added to the grocery list? ")


# Check whether the item is already in the pantry/refrigerator. If it's not, add it to the grocery list.
# Also consider, how will you provide confirmation that the item has been added? Or not added?
if new_item in pantry_fridge:
    print("You already have this item")
else:
    grocery_list.append(new_item)
    print(f"Your item has been added. Your grocery list now contains {grocery_list}")


