import webbrowser
import os, subprocess
new = 2 # open in a new tab, if possible

# clears user.json
open('user.json', 'w')

#  open an HTML file on my own (Windows) computer
url = 'file://' + os.path.realpath('website\\index.html')
webbrowser.open(url,new=new)

subprocess.Popen(f'cd {os.path.realpath("website")}', shell=True)
subprocess.Popen(f'php -S localhost:8000', shell=True)

user = []

while len(user) < 2:
    with open('user.json') as user_input:
        try:
            user = user_input.readlines()
        except:
            pass

subprocess.Popen('exit 1', shell=True)

os.system('python json_to_csv.py')

os.system('python matchmaker.py')

os.system('python city_information.py')