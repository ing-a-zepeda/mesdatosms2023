#Format with %

mass_percentage = "1/6"
print("On the Moon, you would weigh about %s of your weight on Earth" % mass_percentage)


print("""Both sides of the %s get the same amount of sunlight,
... but only one side is seen from %s because
... the %s rotates around its own axis when it orbits %s.""" % ("Moon", "Earth", "Moon", "Earth"))


#Format with method format()

mass_percentage = "1/6"
print("On the Moon, you would weigh about {} of your weight on Earth".format(mass_percentage))

print("""You are lighter on the {0}, because on the {0} 
... you would weigh about {1} of your weight on Earth""".format("Moon", mass_percentage))

print("""You are lighter on the {moon}, because on the {moon} 
... you would weigh about {mass} of your weight on Earth""".format(moon="Moon", mass=mass_percentage))

#Format with f-strings

print(f"On the Moon, you would weigh about {mass_percentage} of your weight on Earth")

round(100/6, 1)

print(f"On the Moon, you would weigh about {round(100/6, 1)}% of your weight on Earth")

subject = "interesting facts about the moon"
f"{subject.title()}"
