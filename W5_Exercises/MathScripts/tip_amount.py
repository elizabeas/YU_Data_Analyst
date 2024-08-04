#Define the known values
food_bill = 75.75
tip_pct = .2

#Calculate the unknown
tip_amt = round((food_bill * tip_pct), 2)
total_w_tip = food_bill + tip_amt

#Display the results
print("The tip on a $" + str(food_bill) + " restaurant bill is $" + str(tip_amt))