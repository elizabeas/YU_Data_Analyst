# Using the range() function:
i = range(5)
print(i)
print(len(i))

# Basic for loop
for i in range(5):
    print(f'Looping {i}')
print('Done')

# Enumerated for loop
fruits = ["apple", "banana", "orange"]
for index, fruit in enumerate(fruits):
    print(f"At position {index}, I found a {fruit}")
veg = 'broccoli'
for i, v in enumerate(veg, 1):
    print(i, v)


# Your little brother has just learned multiplication tables in school. Today he has learned tables of 6 and 7. 
# Help him memorise both the tables by printing them using for loop.
# for i in range(11):
#     print("6 times ", i, " equals ", 6 * i)
# for i in range(11):
#     print(f"7 times {i} equals {7 * i}")

# The following is a list of animals in a National Zoo. 
# Animals = ["lion", "giraffe", "gorilla", "parrots", "crocodile","deer", "swan"]
# Your brother needs to write an essay on the animals whose names are made of 7 letters.
animals = ["lion", "giraffe", "gorilla", "parrots", "crocodile","deer", "swan"]
new_animals = []
for animal in animals:
    if len(animal) == 7:
        new_animals.append(animal)
print(new_animals)



# Basic while loop
i = 0
while i < 3:
    print (f'i = {i}, loop again')
    i = i + 1
print ('Done')


# Starting with the same list of animals from the National Zoo, how would you check for
# animals with 7 letters in the name using a while loop?
animals2 = ["lion", "giraffe", "gorilla", "parrots", "crocodile","deer", "swan"]
new_animals2 = []
i = 0
while i < len(animals2):
    animal = animals2[i]
    if(len(animal)==7):
        new_animals2.append(animal)
    i = i+1
print(new_animals2)

# Using break and continue
