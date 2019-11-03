def get_locations(subject : list):
    index = headers.index('location')
    return subject[index : index + 3]


def get_orientation(subject : list):
    index = headers.index('orientation')
    return subject[index]


def get_age(subject : list):
    index = headers.index('age')
    return int(subject[index])


def get_username(subject : list):
    index = headers.index('username')
    return subject[index]


def check_match(subject : list, match : list):
    subject_location = set(get_locations(subject))
    match_location = set(get_locations(match))

    overlap = set.intersection(subject_location, match_location)

    if len(overlap) == 0:
        return False

    subject_orientation = get_orientation(subject)
    match_orientation = get_orientation(match)

    if subject_orientation != match_orientation:
        return False

    return True


def get_matches(subject : list, population : list):

    for i in range(len(population)):
        if get_username(subject) == get_username(population[i]):
            population.pop(i)
            break
    
    matches = []

    for person in population:
        if check_match(subject, person):
            matches.append(person)

    age_difference = []

    for i in range(len(matches)):
        index = matches[i].index(str(get_age(matches[i])))
        age_difference.append(abs(int(matches[i][index]) - get_age(subject)))

    matches = [x for _,x in sorted(zip(age_difference,matches))]

    return matches


people = []

with open('users.csv') as file_input:
    headers = file_input.readline().replace('\n', '').split(',')

    for line in file_input:
        people += [line.replace('\n', '').split(',')]

subject = people[0]

with open('matches.csv', 'w') as file_output:
    matches = get_matches(subject, people)

    file_output.write('username,common location\n')

    for match in matches:
        location = set.intersection(set(get_locations(subject)), set(get_locations(match))).pop()
        
        file_output.write(f'{get_username(match)},{location}\n')