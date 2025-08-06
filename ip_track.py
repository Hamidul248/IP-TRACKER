# IP LOCATION TRACKER 

import os
import sys
import time

os.system("clear")
print('\n\n')

ab= "\n\n\n\033[1;32m 		SYSTEM INSTALL LOADIND..........\033[1;0m"
os.system('pkg install espeak')
print('\n\n\n\033[1;91m		INSTALL COMPLETE\033[1;0m')
os.system('espeak -a 300 "Install Successfull" ')
print('\n\n\n\033[1;95m		UPDATE SUCCESSFUL ')
os.system('git pull')
os.system('clear')

for c in ab:
	sys.stdout.write(c)
	sys.stdout.flush()
	time.sleep(0.1)

os.system("clear")
print('\n\n\n')
time.sleep(2)

ab= "		\033[1;96mSuccessful Loaded.....\n\033[1;0m"

for c in ab:
	sys.stdout.write(c)
	sys.stdout.flush()
	time.sleep(0.1)
	
print('\n')

name= input('		\033[1;35mYour Name: ')

ab = "	Hey " +name+", Welcome To IP Tracker Tools\033[1;0m"

for c in ab:
	sys.stdout.write(c)
	sys.stdout.flush()
	time.sleep(0.1)
	
print('\n\n')
time.sleep(2)

print('\033[1;32m===================================================\033[1;0m')
ab= (""" \033[1;36m

	 ______  _____   ____   _____   _   _ 
	|___  / / _ \\ \\ / /\\ \\ / / _ \\ | \\ | |
	   / / / /_\\ \\ \V /  \\ \V / /_\\ \\|  \\| |
	  / /  |  _  |\\ /    \\ /|  _  || . ` |
	./ /___| | | || |    | || | | || |\\  |
	\\_____/\\_| |_/\\_/    \\_/\\_| |_/\\_| \\_/
	                                      
		                                      
		______  ___  ___________              
		| ___ \\/ _ \\|_   _|  ___|             
		| |_/ / /_\\ \\ | | | |_                
		|    /|  _  | | | |  _|               
		| |\\ \\| | | |_| |_| |                 
		\\_| \\_\\_| |_/\\___/\\_|                 
		
\033[1;32m===================================================\033[1;0m
\033[1;35m
Owner 		: MOHAMMAD ARAFAT
Tools Name	: IP LOCATION TRACKER
Tools Version 	: 4.2
Github 		: https://github.com/Hamidul248
Facebook	: Mohammad.Arafat.SCFB
		\033[0;92m Use Only Education Purposes
\033[1;32m===================================================\033[1;0m
""")
for c in ab:
	sys.stdout.write(c)
	sys.stdout.flush()
	time.sleep(0.02)

while True:
	username= input('\033[1;32mUser Name : \033[2;0m')
	password= input('\033[1;35mEnter Access Token : \033[1;0m')
	if username == 'ARAFAT' and password == '788' :
		print('	\033[0;1m You Have Successfully Login.')
		os.system('espeak -a 300 " You Have Successfully Login" ')
		break
	else:
		print('\033[0;95mIncorrect Token Number, Please Try Again')
		os.system('xdg-open https://www.facebook.com/Mohammad.Arafat.SCFB')

os.system('clear')
print( " \n\n\n \033[1;35m	WELCOME TO IP LOCATION TRACKER TOOLS\033[1;0m")

import requests 

ip= input('\033[0;1m \033[1;32mEnter Your Target IP : ')

req= requests.get("http://ip-api.com/json/"+ ip)

r= req.json()

print(f'\n 🌍 \033[0;92mCountry :\033[0;93m{r["country"]}')
print(f"\n 📬 \033[0;92mCountry Code :\033[0;93m{r['countryCode']}")
print(f"\n 🧭 \033[0;92m Region : \033[0;93m{r['regionName']}")
print(f"\n 🌐\033[0;92m City : \033[0;93m{r['city']}")
print(f"\n 📟 \033[0;92m Code : \033[0;93m{r['zip']}")
print(f"\n 📶 \033[0;92m Provider : \033[0;93m{r['isp']}")
print(f"\n ☎️ \033[0;92m Organization : \033[0;93m{r['org']}")
print(f"\n 📍 \033[0;92m Lat & Lon : \033[0;93m{r['lat']},{r['lon']}")
print(f"\n 🕛 \033[0;92m Time Zone : \033[0;93m{r['timezone']}")
print(f"\n 📲 \033[0;92m Provider : \033[0;93m{r['as']}\033[0;0m")

print("\033[1;33mLive Location : https:// www.google.com/maps/search/?api=1 & query= {r['lat']},{r['lot']}")

print('\n		✅🔰 \033[1;92mIP Tracking Success')