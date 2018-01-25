#!/usr/bin/python

import sys
import time
import random

bar = 75

print '{................................Loading Game...............................}\n'

sys.stdout.write("[%s]" % (" " * bar))
sys.stdout.flush()
sys.stdout.write("\b" * (bar+1))

for i in xrange(bar):
    time.sleep(0.1)
    sys.stdout.write("=")
    sys.stdout.flush()
sys.stdout.write("\n")

def try_again_1():
    prompt = '> '
    print 'Mai mere un fms ?'
    print '1. Mere'
    print '2. Nu mere'
    mere = int(input(prompt))
    if mere == 1:
        search_wp()
    if mere == 2:
        exit(0)
    else:
        print 'Nu am vz in viata mea o optiune ca asta coaie ce pula mea ?'
def dick():
    print 'Satana mere nu ioo'

def school():
    print 'Scoala'

def main2():
    prompt = '> '
    print 'Unde vrei sa meri?'
    print '1. Pula'
    print '2. Scoala'
    print '3. Exit'
    
    index = int(input(prompt))
    
    if index == 1:
        dick()
    elif index == 2:
        school()
    elif index == 3:
        exit(0)
    else:
        print ('ERROR 404 : Invalid option')

def dungeon():
    prompt = '> '
    boss = 2631
    print 'Boss Health %d' % boss
    print 'COAIE E UN BOSS AICI CAT PULA LUI DUMNEZEU CE O SA FACI ?'
    print '1. Pumn in coaie'
    print '2. RUN BITCH RUUUUUUN'
    decision = int(input(prompt))
    if decision == 1 and weapon or False:
        damage in range(623, 1600)
        print 'i-ai dat %d damage' % damage
        boss -= damage
        time.sleep(0.5)
        if boss < 1:
            print 'you beat the boss'
            time.sleep(5)
            main2()

def search_wp():
    prompt = '> '
    print 'E cam gol aici ce vrei sa faci ?'
    print '1. Cautam Chesti'
    print '2. Plecam'
    bulan = int(input(prompt))
    if bulan == 1:
        print '\nHai Sa Cautam Chestii pe aici poate ai bulan'
        search = '.'
        prog = 18
        sys.stdout.write("Cautam %s" % (" " * prog))
        sys.stdout.flush()
        sys.stdout.write("\b" * (prog+1))
        
        for search in xrange(prog):
            time.sleep(0.2)
            sys.stdout.write(".")
            sys.stdout.flush()
        fms = random.randint(0,9)
        print 'ai gasit un fms +%d' % fms
        print '\nCe vrei sa faci cu el ?'
        print '1. Il testezi' 
        print '2. Pleci'
        print '*atentie fms-ul se poate rupe daca nu il testezi sa fi sigur ca e bun*\n'
        l = int(input(prompt))
        if l == 1:
            print 'Hai sa testam fms-ul sa vedem daca e bun'
            test = 28
            sys.stdout.write("Testam %s" % (" " * prog))
            sys.stdout.flush()
            sys.stdout.write("\b" * (prog+1))
            
            for search in xrange(prog):
                time.sleep(0.2)
                sys.stdout.write("+")
                sys.stdout.flush()
            if fms <> 0:
                print '\namin ca nu e +0\n'
            if fms < 5:
                print 'fms-ul so spart trb sa gasesti minim unu +5 ca sa reziste la bosi'
                print 'soo ne intoarcem'
                search_wp()
            if fms >= 5:
                print 'fms-ul e +%d destul si rezistent cat sa bata un boss' % fms
                weapon = True
                main2()
            time.sleep(5)
        elif l == 2:
            main()
        else:
            print ('ERROR 404 : Invalid option')
    elif bulan == 2:
        main()
    else:
        print ('ERROR 404 : Invalid option')
    
def main():
    prompt = '> '
    print '\nUnde vrei sa meri?'
    print '1. Coridor'
    print '2. Temnita'
    print '3. Pula'
    print '4. Scoala'
    print '5. Exit'
    
    index = int(input(prompt))
    
    if index == 1:
        time.sleep(2)
        search_wp()
    elif index == 2:
        time.sleep(2)
        dungeon()
    elif index == 3:
        time.sleep(2)
        dick()
    elif index == 4:
        time.sleep(2)
        school()
    elif index == 5:
        time.sleep(2)
        exit(0)
    else:
        print ('ERROR 404 : Invalid option')

main()
