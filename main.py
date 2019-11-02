from datetime import date
# prompts user to enter their name
def get_name():
    inputName = 'Please enter your full name: '
    userName = input(inputName)
    return userName

# prompts the user to input what they identify as
def get_identification():
    inputIdentity = 'Please enter what you identify as: '
    userIdentity = input(inputIdentity)
    return userIdentity

# calculates the age of the user using inputted birthday
def get_age(birthday : str):
    # splits the birthday into month, day, and year
    birthday = birthday.split('/')
    birthday = date(int(birthday[2]),int(birthday[0]),int(birthday[1]))
    # gets the date today
    today = date.today()
    # calculates the age of the user
    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
    # returns age
    return age

print('Jake is', get_age('09/12/1998'), 'years old')

# prompts user to enter their top three destinations
def get_destinations():
    inputDestinations = 'Please enter your top 3 countries or states: '
    userDestinations = [input(inputDestinations) for i in range(3)]
    return userDestinations

def get_end_date():
    inputDate = 'Please enter the end date: '
    userDate = input(inputDate)
    return userDate




