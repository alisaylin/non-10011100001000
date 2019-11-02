from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# def airport_from(airport : str):
#     from_ID = 'segments0.origin'

#     # Gets the f
#     from_element = wait.until(EC.((By.ID, from_ID)))

#     # Clears the form so the from airport can be entered
#     from_element.clear()

#     # Sends the from airport to the form
#     from_element.send_keys(airport)

def airport_to(airport : str):
    to_ID = 'segments0.destination'

# Starts the Firefox session
session = webdriver.Firefox()

# Creates the wait function
wait = WebDriverWait(session, 5)

website = 'https://www.aa.com/booking/flights/choose-flights/flight1?bookingPathStateId=1572731422891-682'

session.get(website)

elements = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'row flight-matrix')))

output = [element.get_attribute('innerHTML') for element in elements]

with open('test_data.csv', 'w') as output:
    for thing in output:
        output.write(f'{thing}\n\n\n')