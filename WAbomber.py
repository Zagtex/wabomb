from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def banner():
	print('''
	
 __          __          ____                  _               
 \ \        / /\        |  _ \                | |              
  \ \  /\  / /  \ ______| |_) | ___  _ __ ___ | |__   ___ _ __ 
   \ \/  \/ / /\ \______|  _ < / _ \| '_ ` _ \| '_ \ / _ \ '__|
    \  /\  / ____ \     | |_) | (_) | | | | | | |_) |  __/ |   
     \/  \/_/    \_\    |____/ \___/|_| |_| |_|_.__/ \___|_|   

    Author: 5.h.4.d.0.w

		''')

def main():
	driver = webdriver.Chrome(executable_path="C:\Program Files\Google\Chrome\Application\chromedriver.exe")
	driver.get('https://web.whatsapp.com/')
	time.sleep(5)

	name = input('Enter the name of user or group: ')
	msg = input('Enter your message: ')
	count = int(input('Enter the count: '))

	input('Enter any key after scanning QR code')

	print("*" * 50 + "\n")
	print("Target : {}".format(name))
	print("Message : {}".format(str(msg)))
	print("Amount : {}".format(count))
	print("\n" + "*" * 50)

	if input("Confirm [y/n]?") == 'y':
		pass
	else:
		print("Killed")

	user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
	user.click()

	id_box = driver.find_element_by_id('1234')
	id_box.click()

		
	for i in range(count):
		id_box.send_keys(msg)
		id_box.send_keys(Keys.ENTER)
		time.sleep(0.1)
	print('Bombing Complete!!')

banner()
main()
