# Display an old timey greeting to your friend Ross
print("Hullo, Ross, you old so and so!")


# Calculate the age you'll be this year by subtracting the year you were born from the current year, and display the result
print(2024 - 1981)


# Imagine you are making a delicious brunch for 4 people, and you have one carton of a dozen eggs.
# French toast requires 1 egg per serving. Frittata requires 2 eggs per serving. 
# You're also thinking about making crepes, which takes 2 eggs for the whole batch.
# Do you have enough eggs to make all three recipes? Display the result of your calculation.
print(12 - (4 * 1) - (4 * 2) - 2)


# Pick a 3-digit number. Let's say that's the number of seconds on a timer.
# How many minutes is that? How many remaining seconds, after you calculate the minutes?
print(999 / 60)
print(999 // 60)


# Create variables for each of your favorite foods, including a variable name and the name of the food assigned to that variable.
# Display a list of your favorite foods, starting with "My favorite foods are"
fav1 = 'chicken shahi korma'
fav2 = 'steak with potatoes'
print("My favorite foods are:")
print(fav1)
print(fav2)


# Create a calorie calculator:
# Carbohydrates and proteins contain 4 calories of energy per gram. Fat contains 9 calories per gram.
# Find a food with a nutrition label, and calculate how many calories that food should contain per serving 
# based on the labeled amount of carbohydrate, protein, and fat. Display the result.
carbs = 11 * 4
protein = 12 * 4
fat = 4.5 * 9
print(carbs + protein + fat)


# Create a customer service greeting. First create a variable to ask for the name of the person being greeted.
# Then display the greeting "Welcome, [name]"
name = input("Name? ")
print("Welcome, " + name)


# Create a variable that asks a user to input their birth year. In another variable, calculate their approximate age.
# Then display the result as a sentence in the form of "This year you'll be XX years old"
year_born = input("What year were you born? ")
age = 2024 - int(year_born)
print("This year you will be " + str(age) + " years old")


# Let's update our age calculator with some additional information. Add a conditional statement to determine if the
# user is a member of Gen Z (born 1997-2012) or not, and add that information to the results displayed.
year_born = int(input("What year were you born? "))
age = 2024 - year_born
print("This year you will be " + str(age) + " years old")
if year_born < 2013 & year_born > 1996:
    print("You are a member of Gen Z")
else:
    print("You are not a member of Gen Z")



# How about adding generation labels for Baby Boomers (1946-64), Gen X (1965-80), Millenials (1981-96), and Gen Alpha (2013-present)?
# In that case, how would you modify the "else" message so that it makes more sense?
year_born = int(input("What year were you born? "))
age = 2024 - year_born
print("This year you will be " + str(age) + " years old")
if year_born > 1945 and year_born < 1965:
    print("You are a Baby Boomer")
elif year_born < 1981 and year_born > 1964:
    print("You are a member of Gen X")
elif year_born < 1997 and year_born > 1980:
    print("You are a Millenial")
elif year_born < 2013 and year_born > 1996:
    print("You are a member of Gen Z")
elif year_born > 2012:
    print("You are a member of Gen Alpha")
else:
    print("Your generation cannot be determined")

