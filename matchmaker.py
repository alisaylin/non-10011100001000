# Gets the list of locations from a user
def get_locations(subject : list):

    # Finds the index of the first location element
    index = headers.index('location')

    # Creates a list of all location elements
    return subject[index : index + 3]

# Gets the user's orientation
def get_orientation(subject : list):

    # Finds the index storing orientation data
    index = headers.index('orientation')

    # Returns the user's orientation
    return subject[index]

# Gets the user's age
def get_age(subject : list):

    # Finds the index storing age data
    index = headers.index('age')

    # Returns the user's age
    return int(subject[index])

# Gets the user's username
def get_username(subject : list):

    # Finds the index storing username data
    index = headers.index('username')

    # Returns the user's username data
    return subject[index]

# Checks to see if the subject and potential match are a match
def check_match(subject : list, match : list):

    # Gets the location preferences of both the subject and the match
    subject_location = set(get_locations(subject))
    match_location = set(get_locations(match))

    # Finds the overlap between the subject and match location preferences
    overlap = set.intersection(subject_location, match_location)

    # If there is no location preference overlap it's not a match
    if len(overlap) == 0:
        return False

    # Gets the orientation of both the subject and the match
    subject_orientation = get_orientation(subject)
    match_orientation = get_orientation(match)

    # If the subject and the match don't share the same orientation it's not a match
    if subject_orientation != match_orientation:
        return False

    # All criteria met, it's a match!
    return True

# Gets all matchs a user has and sorts the by age difference (smallest to largest)
def get_matches(subject : list, population : list):

    # Removes the user from potential matches so they don't match with themself
    for i in range(len(population)):

        # Checks if the username of the user matches the username of a potential match
        if get_username(subject) == get_username(population[i]):

            # Removes the user from the potential match list
            population.pop(i)

            # Stop looking for the user in the potential match database
            break
    
    # A list of all confirmed matches
    matches = []

    # Goes through each potential match and checks if they are a match
    for person in population:

        # Checks if they are a match
        if check_match(subject, person):

            # Adds a successful match to the matches list
            matches.append(person)

    # A list storing the age difference between the user and their matches
    age_difference = []

    # Goes through each match and calculates the age difference the user and their matches
    for i in range(len(matches)):

        # Gets the index storing the age of a match
        index = matches[i].index(str(get_age(matches[i])))

        # Calculates the age difference and addeds it to the age difference list
        age_difference.append(abs(int(matches[i][index]) - get_age(subject)))

    # Sorts matches based off age difference
    matches = [x for _,x in sorted(zip(age_difference,matches))]

    # Returns a sorted list of successful matches
    return matches

# An empty list to store all the potential matches
people = []

# Reads the user file
with open('users.csv') as file_input:

    # Adds the file headers to a headers list
    headers = file_input.readline().replace('\n', '').split(',')

    # Goes through each user and adds them to the list of people
    for line in file_input:

        # Adds the person data to the people list
        people += [line.replace('\n', '').split(',')]

# # Sets the subject equal to the first person found
subject = []

with open('subject.csv') as input_file:
    input_file.readline()

    subject = input_file.readline().replace('\n', '').split(',')


# Creates a file storing all successful matches
with open('matches.csv', 'w') as file_output:

    # Creates a list that holds all successful matches
    matches = get_matches(subject, people)

    # The header for the match file
    file_output.write('username,common location\n')

    # Goes through each match
    for match in matches:

        # Adds a common location shared by the user and the match to the file
        location = set.intersection(set(get_locations(subject)), set(get_locations(match))).pop()
        
        # Adds the match's username to the file
        file_output.write(f'{get_username(match)},{location}\n')