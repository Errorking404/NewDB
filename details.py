"""
THIS IS AN OPEN SOURCE PROJECT. A SIMPLE SIM DETAILS FINDER. IT USES API AND REQUEST LIBRARY TO SEND AND RECEIVE DATA.
I WROTE COMMENTS IN EVERY LINE. EXPLAINING THE PROCESS.
MAKE SURE YOU GUYS LEARN SOMETHING INSTEAD OF BEING SCRIPT KIDDIES.

Enjoy guys and create your own tools.
Credits: Error
Author: Error
"""

import requests   #This library is used to send http or https requests
import os         #This one helps user to use linux commands in script. It is used for automation

blu = "\033[94m"  #Blue colour ascii code
grn = "\033[92m"  #Green colour ascii code
red = "\033[91m"  #Red colour ascii code
rst = "\033[0m"   #White colour ascii code
os.system("git pull") #Added this to automatically update the tool directly from GitHub.
banner =os.system("figlet NewDB")  #This line uses is library to create banner. It has nothing to do with core program
print(f"{grn}") #To print text in colour, we 1st create variables,then set their value to ascii color codez, then we use those variables to print color text
print(banner) #This will print banner
print(f"{rst}") #This will set colour back to white
num = input(f"{blu}Enter 11-digit Number (03xx):{rst}") #Here i created num variable and set it to input so user can input 11 digit number or cnic.
url = f'https://sim.f-a-k.workers.dev/?q={num}' #Here is API url. Shotout to FAK bhai for API
r = requests.get(url) # Here i created r variable and used it to call a request function with api parameter

if r.status_code == 200: #Checks if request is successful
    data = r.json() #Another variable named data. r.json is response. Json is a filetype
    if data['status'] == 'success': #Another success check
        for d2 in data['data']: #for loop, this will create new variables like name,cnic,address and mobile and use them to fetch data from Json format.
            name = d2['Name']
            cnic = d2['CNIC']
            address = d2['ADDRESS']
            mobile = d2['Mobile']
            print(f"{grn}")
            print(f"{blu}NAME:{grn}", name) #This will print NAME in blue colour and data in green color
            print(f"{blu}CNIC:{grn}", cnic) #This will print CNIC in blue colour and data in green color
            print(f"{blu}ADDRESS:{grn}", address) #This will print ADDRESS in blue colour and data in green color
            print(f"{blu}MOBILE:{grn}", mobile) #This will print MOBILE in blue colour and data in green color
            print(f"{rst}")
    else:
        print(f"{red}{data['message']}{rst}")
else:
    print(f"{red}Error.{rst}")
