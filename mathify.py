#!/usr/bin/env python3
"""
Mathify will take your puny human language and make it 
mathematically perfect like 01010101010101
https://www.unicode.org/charts/PDF/U2200.pdf
"""
start = '\u2218'
end = '\u2219'
god = '\u222F'
proof = '\u220E'
u = '\u221E'
space = '\u221D'
zero = '\u2205'
one = '{'+zero+'}'+u+zero
two = '{'+ one+'}'+u+one
three = '{'+ two+'}'+u+two
four = '\u222E'
#four = '{'+three +'}'+u+three
five = '{'+four +'}'+u+four
six = '{'+ five+'}'+u+five
seven = '{'+six +'}'+u+six
eight = '\u222F'
#eight = '{'+ seven+'}'+u+seven
nine = '{'+ eight+'}'+u+eight
ten = '{'+ nine+'}'+u+nine
eleven = '{'+ten +'}'+u+ten
#twelve = '{'+eleven+'}'+u+eleven
twelve = '\u2230'
thirteen = '{'+twelve +'}'+u+twelve
fourteen = '{'+ thirteen+'}'+u+thirteen
fifteen = '{'+fourteen +'}'+u+fourteen
sixteen = '\u2237'
#sixteen = '{'+ fifteen+'}'+u+fifteen
seventeen = '{'+sixteen +'}'+u+sixteen
eighteen = '{'+seventeen +'}'+u+seventeen
nineteen = '{'+eighteen+'}'+u+eighteen
twenty = '\u22BD'
#twenty = '{'+nineteen +'}'+u+nineteen
twentyone = '{'+twenty +'}'+u+twenty
twentytwo = '{'+ twentyone+'}'+u+twentyone
twentythree = '{'+twentytwo +'}'+u+twentytwo
twentyfour = '\u22CB'
#twentyfour = '{'+twentythree +'}'+u+twentythree
twentyfive = '{'+twentyfour +'}'+u+twentyfour
twentysix = '{'+twentyfive +'}'+u+twentyfive
twentyseven = '{'+twentysix +'}'+u+twentysix
twentyeight = '\u29DE'
#twentyeight = '{'+twentyseven +'}'+u+twentyseven
twentynine = '{'+twentyeight +'}'+u+twentyeight

Mathify = {
    "2":two,
    "3":three,
    "4":four,
    "5":five,
    "6":six,
    "7":seven,
    "8":eight,
    "9":nine,
    "10":ten,
    "11":eleven,
    "12":twelve,
    "13":thirteen,
    "14":fourteen,
    "15":fifteen,
    "16":sixteen,
    "17":seventeen,
    "18":eighteen,
    "19":nineteen,
    "20":twenty,
    "21":twentyone,
    "22":twentytwo,
    "23":twentythree,
    "24":twentyfour,
    "25":twentyfive,
    "26":twentysix,
    "27":twentyseven,
    "28":twentyeight,
    "29":twentynine,
    "0":zero,
    "1":one,
    "#":space}
