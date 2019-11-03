import random
from random_username.generate import generate_username

# A list of names
name = ['Zoya', 'Callaghan', 'Emily', 'Rose', 'Chase', 'Kyal', 'Morales', 'Merryn', 'Bauer', 'Adrian', 'Lord', 'Zayan', 'Alfaro', 'Annie', 'Cuevas', 'Kya', 'Traynor', 'Barbara', 'Duggan', 'Elif', 'Whitaker']

# A list of locations
location = ['Dallas', 'Seattle', 'Orlando', 'Brooklyn', 'Nashville', 'New Orleans', 'Austin', 'Minneapolis']

# A list of ages
age = [i for i in range(18, 75, 1)]

# A list of orientations
orientation = ['Lesbian', 'Gay', 'Bisexual', 'Transgender', 'Queer', 'Pansexual'] 

# Creates a file storing test user data
with open('users.csv', 'w') as output:

    # Writes a header to the file
    output.write('name,location,location,location,age,orientation,username\n')

    # Generates 100 unique usernames for the users
    username = generate_username(100)

    # Creates 100 fake users
    for i in range(100):

        # Chooses 3 random locations without repeat
        diff_locations = random.sample(location, 3)

        # Chooses a First and Last name
        diff_names = random.sample(name, 2)

        # Adds all the data to a stringe
        line = f'{diff_names[0]} {diff_names[1]},'
        line += f'{diff_locations[0]},{diff_locations[1]},{diff_locations[2]},'
        line += f'{random.choice(age)},'
        line += f'{random.choice(orientation)},'
        line += f'{username[i]}\n'

        # Writes the data to the file
        output.write(line)
