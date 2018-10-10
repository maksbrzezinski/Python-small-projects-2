#! /usr/bin/env python 3
#madLibs.py - reads content of a text file
#and allows to add additional own content in
#place of peculiar words occurence.

import os, sys, re

#TODO: Pobranie danych tekstowych z pliku wskazanego przez użytkownika.
print('Please give a name of a file you want to open.')
swapFile = open(input(), encoding='utf-8')
content = swapFile.read()

#TODO: Odnalezienie i zamiana konkretnych słów.
print('What would you like to put in place of nouns?')
content = re.sub(r'Litwo', input(), content)
print('What would you like to put in place of verbs?')
content = re.sub(r'Ojczyzno', input(), content)
print('What would you like to put in place of adjectives?')
content = re.sub(r'moja', input(), content)
print('What would you like to put in place of adverbs?')
content = re.sub(r'jesteś', input(), content)

#TODO: Zapisanie w nowym pliku tekstowym danych wyjściowych
#i ich wyświetlenie.
with open('replaceTheWords.txt', 'w', encoding="utf-8") as text_file:
    print(f'{content}', file=text_file)
    print('File saved as "replaceTheWords.txt"')
