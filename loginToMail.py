#! /usr/bin/env python 3
#loginToMail.py - Asks for e-mail login and password.
#Logs into an e-mail account and sends an e-mail to
#a desired addressee of a given by a user content.

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import sys, time

#Pobranie od użytkownika loginu i hasła.
print('Please type your gmail login.')
loginInput = input()
print('Please type the password to your email account.')
passwordInput = input()

#Włączenie przeglądarki na stronie GMail.
browser = webdriver.Safari()
browser.get('http://www.gmail.com')

#Wpisanie loginu podanego przez użytkownika i przejście dalej.
login = browser.find_element_by_name('identifier')
login.send_keys(loginInput)
buttonNext = browser.find_element_by_id('identifierNext').click()
time.sleep(2)

#Wpisanie hasła i zalogowanie się do poczty.
password = browser.find_element_by_name('password')
password.send_keys(passwordInput)
loginButton = browser.find_element_by_id('passwordNext').click()
print('''
Zalogowałeś się na swoją pocztę.
Podaj adres email osoby, do której chcesz wysłać maila.
        ''')

#Dodanie adresu email adresata.
sendTo = input()
createNewMsg = browser.find_element_by_id(':i1').click()
time.sleep(1)
toArea = browser.find_element_by_name('to')
toArea.send_keys(sendTo)

#Dodanie treści maila.
messageInput = browser.find_element_by_id(':os')
messageInput.click()
print('Podaj treść wiadomości.')
msg = input()
messageInput.send_keys(msg)

#Wyślij. (Docelowo zapytanie, czy na pewno chcesz wysłać wiadomość.)
sendButton = browser.find_element_by_id(':l3').click()
print('Wiadomość została wysłana.')
