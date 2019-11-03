import random
from random_username.generate import generate_username

name = ['Zoya', 'Callaghan', 'Emily', 'Rose', 'Chase', 'Kyal', 'Morales', 'Merryn', 'Bauer', 'Adrian', 'Lord', 'Zayan', 'Alfaro', 'Annie', 'Cuevas', 'Kya', 'Traynor', 'Barbara', 'Duggan', 'Elif', 'Whitaker']
location = ['Dallas', 'Seattle', 'Orlando', 'Brooklen', 'Nashvil', 'Washington', 'Salt Lake City', 'New York City', 'New Orleans']
age = [i for i in range(18,100,1)]
orientation = ['Straight', 'Gay', 'Lesbian', 'Transgender', 'Queer', 'Bisexual']


with open('test.csv', 'w') as output:
    output.write('name,location,location,location,age,orientation,username\n')

    username = generate_username(100)

    for i in range(100):
        diff_locations = random.sample(location, 3)
        diff_names = random.sample(name, 2)

        line = f'{diff_names[0]} {diff_names[1]},'
        line += f'{diff_locations[0]},{diff_locations[1]},{diff_locations[2]},'
        line += f'{random.choice(age)},'
        line += f'{random.choice(orientation)},'
        line += f'{username[i]}\n'

        output.write(line)