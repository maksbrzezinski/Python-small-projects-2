#! usr/bin/env python 3
#renameDates.py - changes a file name together with date
#in american format MM-DD-YYYY into date in European format DD-MM-YYYY

import shutil, os, re

#Utworzenie wyrażenia regularnego dopasowującego pliki
#zawierające w nazwie datę w formacie europejskim DD-MM-RRRR
datePattern = re.compile(r"""^(.*?) #Cały tekst przed datą.
    ((0|1)?\d)-                     #Jedna, lub dwie cyfry określające miesiąc.
    ((0|1|2|3)?\d)-                 #Jedna, lub dwie cyfry określające dzień.
    ((19|20)\d\d)                   #Cały tekst po dacie.
    (.*?)$
    """, re.VERBOSE)

#TODO: Iteracja przez pliki znajdujące się w katalogu roboczym.
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

#TODO: Pominięcie plików bez daty.
    if mo == None:
        continue

#TODO: Pobranie poszczególnych fragmetów nazwy pliku.
    beforePart  = mo.group(1)
    monthPart   = mo.group(2)
    dayPart     = mo.group(4)
    yearPart    = mo.group(6)
    afterPart   = mo.group(8)

#TODO: Przygotowanie nazwy pliku zawierającej w datę w formacie europejskim.
    euroFilename = beforePart + dayPart + '-' + monthPart + '-'\
    + yearPart + afterPart

#TODO: Pobranie pełnych, bezwzględnych ścieżek dostępu do pliku.
    absWorkingDir   = os.path.abspath('.')
    amerFilename    = os.path.join(absWorkingDir, amerFilename)
    euroFilename    = os.path.join(absWorkingDir, euroFilename)

#TODO: Zmiana nazwy plików.
    print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
    #shutil.move(amerFilename.euroFilename)
        #Usuń komentarz po zakończeniu testów.

