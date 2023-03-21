# Display today's date

from datetime import date

print("Today is: " + str(date.today()))


# Create a variable named parsecs and set it to 11. Then add the code to perform the appropriate calculation and store the result in a variable named lightyears.

parsecs = 11

lightyear = parsecs * 3.26

print(str(parsecs) + " parsecs is: " + str(lightyear) + " lightyears")


parsecs = int(input("Input number of parsecs: "))
lightyears = parsecs * 3.26
print(str(parsecs) + " parsecs is " + str(lightyears) + " lightyears")