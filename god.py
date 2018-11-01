#!/usr/bin/env python3
import mathify
import numberify
"""
A super secret converter
"""
def Process(phrase):
    encoded = ''
    for letter in phrase:
        encoded += mathify.Mathify[numberify.Numberify[letter]]
    #print(encoded)
    return encoded

goAgain = True
while goAgain == True:
    message = ''
    english = list(input("Enter the dialogue you want to Mathify: ").replace(' ', '#'))
    print('Your message became:')
    message = Process(english)
    #print('Your message became:')
    print(message)
