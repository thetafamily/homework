my_favorite_things = {'food': ['burgers', 'pho', 'mangoes'], 'basketball': ['dribbling', 'passing', 'shooting']}
# A list uses square brackets while a dictionary uses curly braces.
my_favorite_things['movies'] = ['Avengers', 'Star Wars']
# my_favorite_things of movies is value
# A square bracket after a variable allows you to indicate which key you're talking about.
print(my_favorite_things['food'])
# We are giving the computer the value of the key food in the variable my_favorite_things.
# We have to be very SPECIFIC in our language on python so the program can understand us.
appliances = ['lamp', 'toaster', 'microwave']
# lists a dictionary were numbers are the keys
print(appliances[1])
appliances[1] = 'blender'
# Use line 12 format to reassign the value the index or position in a list.
print(appliances)
my_favorite_things['movies'].append('Harry Potter')
print(my_favorite_things['movies'])
