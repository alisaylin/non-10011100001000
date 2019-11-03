from datetime import date

# calculates the age of the user using inputted birthday
def get_age(birthday : str):
    # splits the birthday into month, day, and year
    birthday = birthday.split('-')
    
    birthday = date(int(birthday[0]), int(birthday[1]), int(birthday[2]))
    
    # gets the date today
    today = date.today()

    # calculates the age of the user
    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
    
    # returns age
    return age

with open('user.json') as json:
    line = json.readline()

    line = line.replace('[', '').replace(']', '')
    line = line.replace('"', '').replace('\n', '')
    line = line.split(',')

    name = line[0].title()
    age = get_age(line[1])
    username = line[2]


    line = json.readline()

    line = line.replace('[', '').replace(']', '')
    line = line.replace('"', '').replace('\n', '')
    line = line.split(',')

    location = line[0:3]
    orientation = line[4]

with open('subject.csv', 'w') as output:
    output.write('name,location,location,location,age,orientation,username\n')
    output.write(f'{name},{location[0]},{location[1]},{location[2]},{age},{orientation},{username}\n')