with open('match_and_city_info.txt', 'w') as document:
    with open('matches.csv') as matchFile:
        for match in matchFile:
            document.write(f'{match}')
        document.write('\n')
        document.write('City Info:\n')
        with open('city_info.txt') as cityInfo:
            for city in cityInfo:
                document.write(f'{city}')




