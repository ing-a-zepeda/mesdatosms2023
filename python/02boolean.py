# You will start your project by creating the code to determine if a piece of space debris is of a dangerous size. 
# For this exercise we will use an arbitrary size of 5 meters cubed (5m3); anything larger is a potentially dangerous object.
# Add a variable named object_size and set it to 10 to represent 10m3. 
# Then add an if statement to test if object_size is greater than 5. If it is, display a message saying We need to keep an eye on this object. 
# If it's less than 5, display a message saying Object poses no threat.

object_size = 10

if(object_size > 5):
    print("We need to keep an eye on this object.")
else:
    print("Object poses no threat.")

# In the previous exercise you created code to test the size of the object. 
# Now you will test both the object's size and proximity. 
# You will use the same threshold for size of 5m3. If the object is both larger than the threshold and within 1000km of the ship evasive maneuvers will be required.

# For this step you will be presented with the goal for the exercise, followed by an empty cell. 
# Enter your Python into the cell and run it. The solution is at the bottom of the exercise.

# Create two variables: object_size and proximity. Set object_size to 10 to represent 10m3. Set proximity to 9000.
# Then add the code to display a message saying Evasive maneuvers required if both object_size is greater than 5 and proximity is less than 1000. 
# Otherwise display a message saying Object poses no threat.

object_size = 10
proximity = 9000
if object_size > 5 and proximity < 1000:
    print("Evasive maneuvers.")
else:
    print("Object poses no threat.")