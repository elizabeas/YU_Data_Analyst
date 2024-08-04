# Rule of 72:
# (1) Years to double: 72 / Expected rate of return
# (2) Expected rate of return: 72 / Years to double
#
# NOTE: The Rule of 72 could apply to anything that grows at a compounded rate, such as population, 
# macroeconomic numbers, charges, or loans.

# Define the known
start_bal = 5000
end_bal = start_bal * 2
ir = .02

#Calculate the unknown
years = 72 / ir

#Display the results
print('At ' + format(ir, ".0%") + " interest rate, your savings account will be worth " + format(end_bal, ".2f") + " in " + format(years, ".1f") + " years")