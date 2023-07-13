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





# Data structure
'''
List ordered, mutable, allow duplicated values
Tuple ordered, not mutable, allow duplicted values
Set not ordered, mutable, does not allow duplicated values
Dictorionary not ordered, mutable, does not allow duplicated values
'''

#List, to get the position or slice you can use numbers, language[1], language[-1], language[0:2]
language = ["python","java", "golang"]
print(language)

# A list can container another list
language2 = [['python', 'java', 'golang'],'practice', 'dedication']
print(language2[0][0])

# Update values
language[2] = 'Dart'
print(language)

# Add values to list at the end
language.append('golang')
print(language)

# To join 2 lists
otherlanguage = ["C", "C++"]
language.extend(otherlanguage)
print(language)


#Tuples, once defined it cannot be changed
languages  = ("Python", "C", "C++")
print(languages[0])
print(languages[2])


#Dictionary, couple of data replacement of hashmap or json
dictlanguage = {
    "name": "Python",
    "creator": "Guido"
}

print(dictlanguage["creator"])

#To add new couple of data, key and description, this can be a list
dictlanguage["year"] = 1999
dictlanguage["features"] = ['Easy','simple','cool']
print(dictlanguage)

#To update data
dictlanguage["year"] = 1991
print(dictlanguage)

#To recover information it can be used items, keys and values
#items returns tuples
print(dictlanguage.items())
#keys a list with the keys
print(dictlanguage.keys())
#values a list with the values
print(dictlanguage.values())




# Sets contains unique elements
setexample = {1,2,3,4}
setexample2 = {1,1,2.1,"text"}
print(setexample2)

#Add elements to Set
setexample2.add(4)
print(setexample2)

setexample2.update([5,6,7,7])
print(setexample2)

#Delete elements
setexample2.discard(7)
print(setexample2)

setexample2.remove(6) #If element doesn't exist it will thorw a error
print(setexample2)
#Delete all elements
setexample2.clear()
print(setexample2)




#Conditionals



#Cycles