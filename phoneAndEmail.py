#! /usr/bin/env python 3
#phoneAndEmail.py - Seeks for telephone numbers
#and e-mail addresses in a clipboard.

import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              #Numer kierunkowy.
    (\s|'-'|\.)?                    #Separator.
    (\d{3})                         #Pierwsza część numeru.
    (\s|'-'|\.)                     #Separator.
    (\d{4})                         #Druga część numeru.
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  #Numer wewnętrzny
    )''', re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+           #Nazwa użytkownika.
    @                           #Znak @.
    [a-zA-Z0-9.-]+              #Nazwa domeny.
    (\.[a-zA-Z]{2,4})           #Kropka i później cokolwiek.
    )''', re.VERBOSE)

text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Skopiowano do schowka:')
    print('\n'.join(matches))
else:
    print('Nie znaleziono żadnego numeru telefonu lub adresu e-mail.')

