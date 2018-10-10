#! /usr/bin/env python 3
# -*- coding: utf-8 -*-
#randomQuizGenerator.py - Creates quizes
#together with quesetions and answers
#in random order with answer keys.

import random, sys

#To są dane quizu. Klucze to nazwy stanów, natomiast wartości to ich stolice.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'Kalifornia': 'Sacramento', 'Kolorado':
            'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover',
            'Floryda': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii':
            'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield',
            'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
            'Topeka', 'Kentucky': 'Frankfort', 'Luizjana': 'Baton Rouge',
            'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts':
            'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul',
            'Mississippi': 'Jackson', 'Missouri': 'Jefferson City',
            'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
            'Carson City', 'New Hampshire': 'Concord', 'New Jersey':
            'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albans',
            'North Carolina': 'Raleigh', 'North Dacota': 'Bismarck',
            'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon':
            'Salem', 'Pensilvenia': 'Harrisburg', 'Rhode Island':
            'Providence', 'South Carolina': 'Columbia', 'South Dacota':
            'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah':
            'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond',
            'Washington': 'Olimpia', 'West Virginia': 'Charleston',
            'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

#Wygenerowanie 35 plików quizu.
for quizNum in range(35):
    #TODO: Utworzenie plików quizu i odpowiedzi na pytania.
    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')
    
    #TODO: Zapis nagłówka quizu.
    quizFile.write('Full name:\n\nDate:\n\nClass:\n\n')
    quizFile.write((' ' * 20) + 'Capitals Quiz (Quiz %s)' % (quizNum + 1))
    quizFile.write('\n\n')
    
    #TODO: Losowe ustalenie kolejności stanów.
    states = list(capitals.keys())
    random.shuffle(states)
    
    #TODO: Iteracja przez 50 stanów i utworzenie pytania dotyczącego\n
    #każdego z nich.
    for questionNum in range(50):
        #Przygotowanie prawidłowych i nieprawidłowych odpowiedzi.
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

    #TODO: Zapis pytania i odpowiedzi w pliku quizu.
    quizFile.write(('%s. Which city is the capital of %s?\n') % (questionNum + 1, states[questionNum]))
    for i in range(4):
        quizFile.write('    %s. %s\n' % ('ABCD'[i], answerOptions[i]))
    quizFile.write('\n')
    
    #TODO: Zapis odpowiedzi w pliku.
    answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerKeyFile.close()

    
