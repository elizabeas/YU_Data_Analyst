# Description: This script tests various numeric conversion techniques
# Author: Jane Doe-Sample

a = "  101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5  '

# a2 = int(a) # ValueError: invalid literal for int()
b2 = int(b)
# c2 = int(c) # ValueError: invalid literal for int()
# d2 = int(d) # ValueError: invalid literal for int()

a3 = float(a)
b3 = float(b)
# c3 = float(c) # ValueError: could not convert string to float
# d3 = float(d) # ValueError: could not convert string to float

a4 = int(float(a))

a5 = float(a[2:-1])
b5 = int(b[:])
c5 = int(c[0:3])
d5 = int(d[-3])

a6 = a.strip()
d6 = d.strip()

print(b2, type(b2))
print(a3, type(a3))
print(b3, type(b3))
print(a4, type(a4))
print(a5, type(a5))
print(b5, type(b5))
print(c5, type(c5))
print(d5, type(d5))
print(a6, type(a6))
print(d6, type(d6))