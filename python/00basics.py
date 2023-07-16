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
#equal "=="
#not equal "!="
#lower than "<"
#greater than  ">"
#lower equal "<="
#greater equal ">="
#validate same object "is"
#and
#or
#not

a = 1
b = 2
if a < b:
    print("a is lower than b")
elif a==b:
    print("a is equal b")
else:
    print("b is greater than a")





#Cycles
# For cycle
for letra in "texto":
    print(letra)

for i in range(1,5):
    print(i)

# While cycle
i = 10
while i <= 15:
    print(i)
    i += 1

# For with list
language = ['python', 'golang','C']

for lang in language:
    print(lang)

# For with dictionary
language = {
    "name": "Python",
    "creator": "Guido Van Rossum"
}

for key in language:
    print("key:", key, " value:", language[key])

# Functions
# function with no parameters
def firstfunction():
    print("First function")

firstfunction()

# function with parameters
def perimeter_square(side, units):
    perimeter = side * 4;
    print("Perimeter is:",perimeter, units)

perimeter_square(10, "cm")
perimeter_square(units = "in", side=5)

# function that returns a result
def area_square(side):
    return side*side
area =area_square(5) 
print(area)

# function that returns more than 1 result, it returns a tuple
def square(side):
    return side*4, side*side
area =square(5) 
print("Perimeter:",area[0], " Area:", area[1])

# function with documentation (Doc styles: NumPy/SciPy docstrings, PyDoc, EpyDoc, Google Docstrings)

def square_operations(side):
    ''' Function will calculate perimeter and area from a square

        This function will receive the value from the lenght of the side,
        with this information it will calculate perimeter and area.

        Args:
            side(int): Lenght from the side of a square
        
        Returns:
            perimeter(int): Perimeter from the square, position 0 from tuple
            area(int): Area from the square, position 1 from tuple
        
    '''
    return side*4, side*side

square_operations(5)





# Modules and Packages
#Standar python libraries:
#Alias can be applied by import datetime as dt
#Specific methods can be called by from datetime import datetime
import datetime
hour_now = datetime.datetime.now()
print(hour_now)


#Create own module:
#1st create a new file
#2nd create functions inside new file
#3rd if file is in same path just call file like this:

from circle import circle_area, circle_perimeter

diameter = 5

circle = {
    "diameter" : diameter,
    "area" : circle_area(diameter),
    "perimeter" : circle_perimeter(diameter)
}

print(circle)


#Packages
#store modules similar between them
#Create a new directory inside create a __init__.py file
#create files with methods
#from main call
from figures.square import square_area, square_perimeter
from figures.circle import circle_area, circle_perimeter

side = 4
square1 = {
    "side" : side,
    "area" : square_area(side),
    "perimeter" : square_perimeter(side)
}

diameter = 4
circle1 = {
    "diameter" : diameter,
    "area" : circle_area(diameter),
    "perimeter" : circle_perimeter(diameter)
}

print(square1)
print(circle1)


#POO
#Name in camel case, fist letter in uppecase
class Person:
    attribute = 123
    def __init__(self, name, age):
        #print("I'm in the constructor")
        self.name = name
        self.age = age
    def birthday(self):
        self.age += 1
        print(f"Happy birthday #{self.age} {self.name}")

peter = Person("Peter", 20)
paul = Person("Paul", 30)
print(type(peter), type(paul))
print(peter.name)
print(peter.attribute)
print(paul.age)
print(paul.attribute)


print(peter.name, peter.age)
peter.birthday()

#Class son from Person
class Employee(Person):
    def __init__(self, total_hours,name, age):
        super(Employee, self).__init__(name, age)
        self.total_hours=total_hours
    def work(self, hours):
        self.total_hours += hours
        print("you have worked", hours,"hours")
        print("Total hours:", self.total_hours)

peter2 = Employee(name= "Peter", age = 20, total_hours=30)
peter2.work(8)
peter2.birthday()





# Packages could be gotten from pypi.org
# to install it is required to use pip command, from CMD or terminal not python started
# pip --version                to validate pip version and python version
# pip install flask            to install flask library
# pip install pandas=1.3.4     to install an specific version
# pip freeze                   to get all the libraries installed
# pip uninstall pandas         to uninstall pandas library



# Virtual environments
# virtualenv, venv, anaconda or conda.
# To install VirtualEnv we require:
# Open terminal and install with: pip install virtualenv
# once installed go to the project path and type: virtualenv env
# then write on windows: env\Scripts\activate             for linux/mac:  source env\bin\activate
# to deactivate environment just type: deactivate
# to delete environment: rm dir env /s                    for linux/mac: rm -f env


# requirements files contains all needed for project, 
# requirements.txt must be created
#example:
# flask == 2.0.2

#once activated environment use pip to install: pip install -r requirements.txt
#then: pip freeze





#Errors
# Syntax, zero division, data missmatch
# errors can stop a script running, to avoid it we can use try-except

def average_calculation(list1):
    #assert len(list) > 0
    numsum = 0
    for i in list1:
        numsum += i

    lenght = len(list1)

    return numsum/lenght

#empty list
try:
    average=average_calculation(list1=[])
    print(average)
except:
    print("function couldn't calculate average")

#empty list with exception
try:
    average=average_calculation(list1=[])
    print(average)
except Exception as e:
    #print("function couldn't calculate average")
    print(e)
#list with data
try:
    average=average_calculation(list1=[1,2,3])
    print(average)
except:
    print("function couldn't calculate average")
