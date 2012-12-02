#!/usr/bin/env python
#encoding: utf-8

import re


def main():
    file = open('answer.txt', 'w')
    correct = False
    pattern = '[n|N]iebieski'
    pattern = re.compile(pattern)
    while correct == False:
        ans = raw_input('Jakiego koloru jest niebo? \n' +
                    'A: Czerwonego \n' +
                    'B: Niebieskiego \n')
        find = re.match(pattern, ans)
        if ans == "Niebieskiego" or ans == 'B' or find:
            correct = True
            print 'OK! nastepne pytanie \n'
        else:
            print 'Bledna odpowiedz, sprobuj raz jeszcze.'

    file.write('Odpowiedz 1. (kolor nieba) \n \t %s \n' % ans)

    correct = False
    while not correct:
        ans  = raw_input('Kto jest autorem tego programu? \n')
        if ans == 'Bogna Knychala':
            correct = True
            print 'OK! nastepne pytanie \n'
        else:
            print 'Bledna odpowiedz, sprobuj raz jeszcze. \n'
            print 'Podopowiedz: Bogna Knychala :) \n'

    file.write('Odpowiedz 2. (imie i nazwisko autora) \n \t %s \n' % ans)

    ans = raw_input('Jak sie nazywasz? \n')
    print 'OK! nastepne pytanie \n'

    file.write('Odpowiedz 3. (imie i nazwisko uzytkownika) \n \t %s \n' % ans)

    correct = False
    while not correct:
        ans = raw_input("Czy ten program jest latwy w uzyciu \n")
        if len(ans) > 0:
            if 0 <= int(ans) and int(ans) <= 3:
                correct = True
                print 'OK! nastepne pytanie \n'
            else:
                print 'Bledna odpowiedz, odpowiedz musi miescic sie w skali od 0-3 \n'
        else:
            print 'Bledna odpowiedz, odpowiedz musi miescic sie w skali od 0-3 \n'

    file.write('Odpowiedz 4. (latwosc programu w skali 0-3) \n \t %s \n' % ans  )

    ans = raw_input('Co nie odpowiadalo Ci w tym programie? \n')
    print 'Dziekuje \n'

    file.write('Odpowiedz 5. (opinia uzytkownika) \n \t %s \n' % ans  )

    print 'Odpowiedzi zostaly zapisane w pliku answer.txt'

    file.close()


main()