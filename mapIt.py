#! /usr/bin/env python 3
#-*- coding: utf-8 -*-
#mapIt - Displays a map in a browser based
#on either address given in a terminal, or
#an address in a clipboard.

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    #Pobranie adresu wiersza poleceń
    address = ' '.join(sys.argv[1:])
else:
    #Pobranie adresu ze schowka.
    address = pyperclip.paste()

webbrowser.open('http://www.google.pl/maps/place/' + address)

#TODO: Pobranie adresu ze schowka.
