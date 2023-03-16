# Create dictionary
planet = {
    'name': 'Earth',
    'moons': 1
}

# Read data
print(planet.get('name'))
print(planet['name'])

# Add data
planet.update({'name': 'Makemake'})

planet['name'] = 'Makemake'

# Using update
planet.update({
    'name': 'Jupiter',
    'moons': 79
})

# Using square brackets
planet['name'] = 'Jupiter'
planet['moons'] = 79

# Add keys
planet['orbital period'] = 4333

#Delete keys
planet.pop('orbital period')


# Complex dictionaries
planet['diameter (km)'] = {
    'polar': 133709,
    'equatorial': 142984
}

print(f'{planet["name"]} polar diameter: {planet["diameter (km)"]["polar"]}')


# Recover all keys and values with cycle
rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}

for key in rainfall.keys():
    print(f'{key}: {rainfall[key]}cm')

# Search for a key, if doesn't exist create it
if 'december' in rainfall:
    rainfall['december'] = rainfall['december'] + 1
else:
    rainfall['december'] = 1

# Recover all the keys and values
total_rainfall = 0
for value in rainfall.values():
    total_rainfall = total_rainfall + value

print(f'There was {total_rainfall}cm in the last quarter')