from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
import urllib, re
import urllib.request
from bs4 import BeautifulSoup

# returns article of top things to do in given city
def get_article(city : str):
    
    options = Options()
    # makes the browser headless
    options.headless = True
    # creates a Firefox session
    session = webdriver.Firefox(options=options)

    # modifies city to match website 
    city = city.lower().replace(' ', '-')
    keyword = 'Best Things to Do in'
    website = 'https://www.thecrazytourist.com/?s=' + city

    wait = WebDriverWait(session, 3)
    session.get(website)

    # gets the link of the article 
    link = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, keyword)))
    article = link.get_attribute('href')
    print(article)
    session.close()
    return article

# web scrapes and gets the top list of activities to do in city
def get_activities(article : str):
    html = urllib.request.urlopen(article)
    soup = BeautifulSoup(html, 'lxml')
    tags = soup.findAll('h2')
    activities = []

    for tag in tags[1:-3]:
        tag = tag.text.split('. ')[-1]
        activities.append(tag)
    return activities

# creates a csv file of activity list
def activities_to_csv(activities : list):
    with open('activities.csv', 'w') as activityFile:
        for activity in activities:
            activityFile.write(activity + '\n')
    activityFile.close()
    print('Done. Check the activities.csv')

cities = []
with open('matches.csv','r') as cityFile:
    cityFile.readline()
    for line in cityFile:
        line = line.replace('\n', '').split(',')
        cities += [line[1]]
cities = set(cities)
print(cities)
with open('city_info.txt', 'w') as cityInfo:
    for city in cities:
        print(city)
        cityInfo.write(f'{city.title()}\n')
    
        for activity in get_activities(get_article(city)):
            cityInfo.write(f'- {activity}\n')
        cityInfo.write('\n')
