#! /usr/bin/env python 3
#loginToMail.py - Asks for e-mail login and password.
#Logs into an e-mail account and sends an e-mail to
#a desired addressee of a given by a user content.

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import sys, time

#Get login and password
print('Please type your gmail login.')
loginInput = input()
print('Please type the password to your email account.')
passwordInput = input()

#Go to GMail in a browser
browser = webdriver.Safari()
browser.get('http://www.gmail.com')

#Parse login obtained earlier
login = browser.find_element_by_name('identifier')
login.send_keys(loginInput)
buttonNext = browser.find_element_by_id('identifierNext').click()
time.sleep(2)

#Parse password obtained earlier and log in
password = browser.find_element_by_name('password')
password.send_keys(passwordInput)
loginButton = browser.find_element_by_id('passwordNext').click()
print('''
You are logged in to you email account.
Type email address of your recipient.
        ''')

#Add recipient email address
sendTo = input()
createNewMsg = browser.find_element_by_id(':i1').click()
time.sleep(1)
toArea = browser.find_element_by_name('to')
toArea.send_keys(sendTo)

#Add email content
messageInput = browser.find_element_by_id(':os')
messageInput.click()
print('Add message.')
msg = input()
messageInput.send_keys(msg)

#Send.
sendButton = browser.find_element_by_id(':l3').click()
print('The email is sent.')
