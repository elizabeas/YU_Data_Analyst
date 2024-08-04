word = 'banana'
num = 12
num = num + 1
word = word + '12'

#False = 'farts'

import math

# var = 'house'
# print(var[0:2])
# print(var[:2])
# print(var[2:4])
# print(var[2:-1])
# print(var[2:])

# string1 = "banana apple orange"
# words1 = string1.split()
# print(words1)
# print(type(words1))

# string2 = "banana, apple, orange"
# words2 = string2.split(',')
# print(words2)
# print(type(words2))

# string2 = "banana, apple, orange"
# words3 = string2.split('a')
# print(words3)
# print(type(words3))

# if num + num > num:
#     print("That makes sense")
# else:
#     print("What?")

# x = input("Test value for x (must be a number!): ")
# y = input("Test value for y (must be a number!): ")

# if x < y:
#    print("x is bigger")
# elif float(x) == float(y):
#    print("x and y are the same")
# else:
#    print("x is less than y")

# num_kids = int(input("How many kids? "))
# price = num_kids * 9.95    # price is $9.95/kid
# if num_kids >= 6:       
#    price = price * .9      # a 10% discount
#    print(price)
# else:
#     print(price)

# sale_amt = float(input("Sale amount: "))
# tax = round(sale_amt * .08, 2)   # 8% sales tax
# tax_exempt = input("Tax exempt? (Y/N) ")
# if (tax_exempt == 'Y'):
#      tax = 0
# print(tax)

#print(bool(''))

# greeting = 'Hello, World!'
# match greeting:
#     case 'Hello, World!':
#         print('Hello to you too!')
#     case 'Goodbye, World!':
#         print('See you later')
#     case other:
#         print('No match found')


strawb = input('Strawberry? Y/N: ')
blueb = input('Blueberry? Y/N: ')
fresh = input('Are the berries fresh? Y/N: ')
if (strawb =='Y' or blueb =='Y') and fresh == 'Y':
    print('Buy it!')
else:
    print("Don't buy it") 
