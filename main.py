#! /usr/bin/python3

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException 


print(
"""



\t\t\t\t\t\t██  ██████      ██████   ██████  ████████ 
\t\t\t\t\t\t██ ██           ██   ██ ██    ██    ██    
\t\t\t\t\t\t██ ██   ███     ██████  ██    ██    ██    
\t\t\t\t\t\t██ ██    ██     ██   ██ ██    ██    ██    
\t\t\t\t\t\t██  ██████      ██████   ██████     ██     - By Mansi
                                          
                                          

"""
	)       


def printGreen(text):
	print("\033[92m{}\033[00m" .format(text))

def printPurple(text): 
	print("\033[95m{}\033[00m" .format(text))

def printRed(text): 
	print("\033[91m{}\033[00m" .format(text))

try:
	chatbot = ChatBot("Mansi's chatbot",
	    storage_adapter='chatterbot.storage.SQLStorageAdapter',
	    logic_adapters=[
	        'chatterbot.logic.MathematicalEvaluation',
	        #'chatterbot.logic.TimeLogicAdapter',
	        'chatterbot.logic.BestMatch',
	        {
	            'import_path': 'chatterbot.logic.SpecificResponseAdapter',
	            'input_text': 'help',
	            'output_text': 'here is a link: http://chatterbot.rtfd.org'
	        }
	        
	     ],
	    database_uri='sqlite:///database.db'
	)


	conversation = [
	    "Hello",
	    "Hi there!",
	    "How are you doing?",
	    "I'm doing great.",
	    "That is good to hear",
	    "Thank you.",
	    "You're welcome.",
	    "who made you?",
	    "Mansi made me under Jeet's guidance",
	]

	printGreen("Loading Corpus...\n")

	trainer = ListTrainer(chatbot)

	trainer.train(conversation)

	trainer = ChatterBotCorpusTrainer(chatbot)

	trainer.train(
	    "chatterbot.corpus.hindi"
	)

	def finding_path(xpath):
	    flag = False

	    while (flag == False):
	      
	        try:
	            driver.find_element_by_xpath(xpath)
	            flag = True

	        except NoSuchElementException:
	            #print("Finding path...")
	            pass

	    return flag

	printGreen("\nEnter Instagram Credentials -  \n")

	username_id = input("\033[95mUsername: \033[00m")
	username_password = input("\033[95mPassword: \033[00m")

	driver = webdriver.Firefox()

	driver.get("https://www.instagram.com/")

	username = "html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input"

	password = "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input"

	login = "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]"

	save = "/html/body/div[1]/section/main/div/div/div/div/button"

	notnowbutton = "/html/body/div[4]/div/div/div/div[3]/button[2]"

	signmsg = "/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]/a/div/div[3]/div"

	user1 = "/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]/a/div"

	userpath = "/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]/a/div/div[2]/div[1]/div/div/div/div"

	msg_to_send = "/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea"

	send_button = "/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button"

	check_user = finding_path(username)

	try:
	    if check_user:

	        driver.find_element_by_xpath(username).send_keys(username_id)

	        driver.find_element_by_xpath(password).send_keys(username_password)

	        driver.find_element_by_xpath(login).click()

	        check_save_popup = finding_path(save)

	        if check_save_popup:

	        	printGreen("\nLogin Successfully! \n\nBot is running....")
		        driver.find_element_by_xpath(save).click()

		        check_notnow = finding_path(notnowbutton)

		        if check_notnow:

		            driver.find_element_by_xpath(notnowbutton).click()

		            while True:

		                driver.get("https://www.instagram.com/direct/inbox/")

		                check_msg = finding_path(signmsg)

		                if check_msg:

		                    #print("new msg")

		                    print("\n")

		                    firstuser = driver.find_element_by_xpath(userpath).text

		                    driver.find_element_by_xpath(user1).click()

		                    counter = 1

		                    while True:
		                        """
		                        a = driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/div[6]/div[2]/div").text
		                        print(a)
		                        """
		                        try:
		                            
		                            finding_last_msg_xpath = "/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/div[" + str(counter) + "]/div[2]/div"

		                            last_message = driver.find_element_by_xpath(finding_last_msg_xpath).text

		                            #print(last_message)
		                            
		                            counter = counter + 1

		                        except NoSuchElementException:
		                            
		                            #print("There's no message with ID: " + str(counter))

		                            counter = counter + 1

		                            if counter > 50:

		                                print(firstuser + ": " + last_message)
		                                
		                                counter = 1
		                                
		                                break

		                    bot_response = chatbot.get_response(last_message)

		                    driver.find_element_by_xpath(msg_to_send).send_keys(str(bot_response))

		                    driver.find_element_by_xpath(send_button).click()

		                    print("Bot: " + str(bot_response))

	except (KeyboardInterrupt, EOFError, SystemExit):
		printRed("\n\nUser Requested An Interrupt")
		printRed("Apllication Shutting Down")
		printRed("Closing Instagram Bot")
		driver.quit()

except KeyboardInterrupt:
	printRed("\n\nUser Requested An Interrupt")
	printRed("Application Shutting Down")

