PASSWORT = '1234'

import sys

import random

import time

import os

def hauptmenu():
    print ('---------------Menu---------------')
    print ('      Type 1 to view Info')
    print ('      Type 2 for help')
    print ('      Type 3 to restart program')
    print ('      Type 4 for "Guessing Game"')
    print ('      Type 5 to close program')
    print ('----------------------------------')

def INFOS():
    print ('----------INFORMATION----------')
    print ('    Name: Mateja')
    print ('    Hobbies: Music, IT, HiFi')
    print ('-------------------------------')

def NICHT_VERSTEHEN():
    print ()
    print ('------------------------------------------------------')
    print ('If you dont understand something, please write "help".')
    print ('------------------------------------------------------')
    print ()

def random_zahl_spiel_erklärung():
    print ('You need to choose a number between 1-10. The program is going to choose the winning number and if you have chosen that exact number your will win the game.')

def abstand():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

def lade_animation():
    for _ in range(3):
        animation = [".  ", ".. ", "..."]
        for i in animation:
            print (f"\rStarting MatEjaOS 1.0, please wait{i}", end="")
            time.sleep(0.6)

lade_animation()
abstand()
print("Loading complete, welcome to MatEjaOS 1.0!")
time.sleep(2)
programm_neustart = False
def MatEjaOS():
    global programm_neustart
    abstand()
    modus = 'passwort'
    while True:
        if modus == 'passwort':
            if programm_neustart:
                print ('Programm has been successfully restarted.')
                programm_neustart = False
            NICHT_VERSTEHEN()
            passwort_eingabe = input('Enter password:')        
            if passwort_eingabe.lower() == 'help':
                abstand()
                print ('You need to enter youre Password, because the following informations must be kept private and P.S the password is "1234"')
                continue
            if passwort_eingabe == PASSWORT:
                abstand()
                print ('Welcome back, Mateja!')
                modus = 'menu1'
            else:
                abstand()
                print ('WRONG PASSWORT! Try looking for -->HELP<--')

        elif modus == 'menu1':
            hauptmenu()
            wahl=input('Enter youre number here:')
            if wahl == '1':
                abstand()
                INFOS()
            elif wahl == '2':
                abstand()
                print ('Please write a number depending on what you need.')
            elif wahl == '3':
                programm_neustart = True
                abstand()
                break
            elif wahl == '4':
                random_zahl_spiel_erklärung()
                random_zahl_spiel_wahl = input('ENTER A NUMBER:')
            elif wahl == '5':
                print ('Closing programe, please wait...')
                sys.exit()
            else:
                abstand()
                print ('Please enter a valid Number!')
while True:
    MatEjaOS()
