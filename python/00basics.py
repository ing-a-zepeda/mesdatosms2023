# comment
print("hello world") #comment inline

''' multi
line
comment '''


# Variables

# String
name = "Alfonso"

# Numeric: Integer or Float
age = 36
height = 1.70

# Boolean
positive = True
negative = False


#Find what kind of variable
print(type(name))
print(type(age))
print(type(height))
print(type(positive))



#Operators
#Math Operators
#add
sum = 1+1
#substraction
sub = 1-1
#multiplication
mult = 1*2
#division
div = 50/10
#Modulus
mod = 50%11
#Exponetiation
exp = 2 ** 3
#Floor division
floordiv = 50//11

# Bit wise operators
# AND & Sets each bit to 1 if both bits are 1
y = 4 & 5

# OR | Sets each bit to 1 if one of both bits are 1
y = 4 | 5

# XOR ^ sets each bit to 1 if only one of two bits is 1
y = 1 ^ 2

# NOT ~ invert all the bits
y = ~2

# << Shift left by pushing zeros in from the right and let the leftmost bits fall off
y << 2

# >> Shift right by pushing copies of the leftmost bit from the left nd let the rightmost bits fall off
y >> 2



# Logical operators
# and returns true if both statemts are true
m = 2
z = m < 5 and m < 10

# or returns True if one of the statements is true
m = 2
z = m < 5 or m < 10

# not reverse the result, it changes False to True and True to False
m = 2
z = not(m < 5 and m < 10)



# Identity operators
# is Return true if both variables are same object
a = 1
b = 1
a is b

# is not return true if both variables are not the same object
b is not a



# Membership operators
# in returns true if a sequence with the specified value is present in the object
b = []
a in b

# not in returns true if a sequence with the specified value is not present in the object
a not in b



#Assigment Operators
x = 5

#Add and assign
x += 5 # x = x + 5

#Substraction and assign
x -= 5 # x = x - 5

#Multiplication and assign
x *= 5 # x = x * 5

#Division and assign
x /= 5 # x = x / 5

#Modulus and assign
x %= 5 # x = x + 5

#Floor division and assign
x //= 5 # x = x // 5

#Exponetiation and assign
x **= 5 # x = x ** 5

#
x = 5
x &= 5 # x = x & 5

#
x |= 5 # x = x | 5

#
x ^= 5 # x = x ^ 5

#
x >>= 5 # x = x >> 5

#
x <<= 5 # x = x << 5