# python -m pip install selenium
# pip install asyncio
# python.exe -m pip install --upgrade pip
from asyncio import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, random

# Username and password of your instagram account:
my_username = 'username'
my_password = 'password'

# Instagram username list for DM:
usernames = ['user1', 'user2', 'user3']

# Messages:
messages = ['Hey', 'how you doing?', 'Hi']

# Delay time between messages in sec:
between_messages = 2000

#browser = webdriver.Chrome('chromedriver')
#driver = webdriver.Chrome('chromedriver')
driver = webdriver.Chrome(executable_path="C:\\Users\\USER\\Desktop\\ICT\\GitHub\\Python---Programs\\Inst messsage\\chromedriver.exe")
#driver = webdriver.Edge(executable_path="C:\\Users\Abhishek Sharma\\OneDrive\Desktop\\ICT Sem 3\\Programming with Python\\Project\\Program\\msedgedriver.exe")
#driver = webdriver.Firefox(executable_path="C:\\Users\Abhishek Sharma\\OneDrive\Desktop\\ICT Sem 3\\Programming with Python\\Project\\Program\\geckodriver.exe")
#driver = webdriver.Firefox(executable_path="C:\\Users\Abhishek Sharma\\OneDrive\Desktop\\ICT Sem 3\\Programming with Python\\Project\\Program\\setup-stub.exe")

# Authorization:
def auth(username, password):
	try:
		driver.get('http://instagram.com')
		time.sleep(random.randrange(1,2))
		#sleep(10000)

		input_username = driver.find_element_by_name('username')
		input_password = driver.find_element_by_name('password')

		input_username.send_keys(username)
		time.sleep(random.randrange(1,2))
		input_password.send_keys(password)
		time.sleep(random.randrange(1,2))
		input_password.send_keys(Keys.ENTER)

	except Exception as err:
		print(err)
		webdriver.quit()
  
auth(my_username, my_password)

# Sending messages

def send_message(users, messages):
	try:
		driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()
		time.sleep(random.randrange(3,5))
		driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()
		time.sleep(random.randrange(1,2))
		driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div/div[3]/div/button').click()
		for user in users:
			time.sleep(random.randrange(1,2))
			driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(user)
			time.sleep(random.randrange(2,3))
			driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[2]/div[1]').find_element_by_tag_name('button').click()
			time.sleep(random.randrange(3,4))
			driver.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/div/button').click()
			time.sleep(random.randrange(3,4))
			text_area = driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
			text_area.send_keys(random.choice(messages))
			time.sleep(random.randrange(2,4))
			text_area.send_keys(Keys.ENTER)
			print(f'Message successfully sent to {user}')
			time.sleep(between_messages)
			driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button').click()

	except Exception as err:
		print(err)
		webdriver.quit()

auth(my_username, my_password)
time.sleep(random.randrange(2,4))
send_message(usernames, messages)