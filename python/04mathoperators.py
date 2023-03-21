# Arithmetic operators in Python
# Python provides common arithmetic operators so you can perform mathematic operations in your code. 
# These include the four core operations of addition, subtraction, multiplication, and division.

# Start by using two planet distances: Earth (149,597,870 km) and Jupiter (778,547,200 km).
# Create variables to store the distances
# Start by creating two variables named first_planet and second_planet. 
# Set first_planet to the distance from the sun to Earth, and second_planet for the distance from the sun to Jupiter.

first_planet = 149597870
second_planet = 778547200

# You can subtract these two values to determine the distance between the planets.
# Start by adding the code to subtract first_planet from second_planet and store the result in a variable named distance_km. Display the value to the screen.
# Then add the code to convert distance_km to miles by dividing it by 1.609344 (the rough difference between miles and kilometers) and store the result in a variable named distance_mi. 
# Display the value to the screen.

distance_km = second_planet - first_planet
print(distance_km)

distance_mi = distance_km / 1.609344
print(distance_mi)


# We want to read the distance from the sun for two planets, and then display the distance between the planets. 
# We'll do this by using input to read the values, int to convert to integer, and then abs to convert the result into its absolute value.

# Start by adding the code to prompt the user for the distance between the sun and the first planet, and then the second. 
# Store each result in variables named first_planet_input and second_planet_input.
    

first_planet_input = input('Enter the distance from the sun for the first planet in KM')
second_planet_input = input('Enter the distance from the sun for the second planet in KM')

# Because input returns string values, we need to convert them to numbers. 
# Add the code to convert each input into an integer using int. 
# Store the values in first_planet and second_planet respectively.

first_planet = int(first_planet_input)
second_planet = int(second_planet_input)

# Subtracting the first planet from the second. 
# Because the second planet might be a greater number, you'll use abs to convert it to an absolute value.

# Subtract first_planet from second_planet and convert the result to its absolute value by using abs. 
# Store the result in a variable named distance_km. Then display the result on the screen.

distance_km = second_planet - first_planet
print(abs(distance_km))

# Planet	Distance from sun
# Mercury	57900000
# Venus     108200000
# Earth     149600000
# Mars  	227900000
# Jupiter	778600000
# Saturn	1433500000
# Uranus	2872500000
# Neptune	4495100000

#########
# Conversion from string to number
demo_int = int('215')
print(demo_int)

demo_float = float('215.3')
print(demo_float)

# Absoulte values
print(abs(39 - 16))
print(abs(16 - 39))

# Round
print(round(14.5))

# Math library
from math import ceil, floor

round_up = ceil(12.5)
print(round_up)

round_down = floor(12.5)
print(round_down)