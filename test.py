#!/usr/bin/python

import sys
import time
import random

weapon = False
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

def dick():
    print 'Satana mere nu ioo'

def dye():
    print 'Imi pare bine ca ai jucat'
    print 'Dar esti praf'
    time.sleep(5)
    exit(0)

def school():
    print 'Scoala'

def main2():
    prompt = '> '
    print 'Unde vrei sa meri?'
    print '1. Temnita'
    print '2. Pula'
    print '3. Scoala'
    print '4. Exit'
    
    index = int(input(prompt))

    if index == 1:
        time.sleep(2)
        dungeon()
    elif index == 2:
        time.sleep(2)
        dick()
    elif index == 3:
        time.sleep(2)
        school()
    elif index == 4:
        time.sleep(2)
        exit(0)
    else:
        print ('ERROR 404 : Invalid option')

def dungeon():
    prompt = '> '
    player = random.randint(1000,3000)
    boss = random.randint(1000,3000)
    print 'Your Health %d' % player
    print 'Boss Health %d' % boss
    print 'Aici e un boss ce o sa faci ?'
    print '1. Pumn in coaie cu fms'
    print '2. RUN BITCH RUUUUUUN'
    decision = int(input(prompt))
    if decision == 1:
        while True:
            damage = random.randint(623, 1600)
            damage_boss = random.randint(623, 1600)
            time.sleep(0.5)
            print 'Vrei sa il ataci sau sa te retragi ?'
            print '1. Ataca'
            print '2. Retragete'
            ppwp = int(input(prompt))
            if ppwp == 1:
                print 'i-ai dat %d damage' % damage
                time.sleep(0.5)
                print 'boss-ul mai are %d viata' % boss
                boss -= damage
                print 'ti-a dat %d damage' % damage_boss
                time.sleep(0.5)
                print 'mai ai %d viata' % player
                player -= damage_boss
                time.sleep(0.5)
                if boss < 10:
                    print 'ai infrant boss-ul'
                    time.sleep(5)
                    main2()
                if player < 10:
                    print 'ai murit....'
                    time.sleep(5)
                    dye()
            elif ppwp ==2:
                time.sleep(5)
                main()
            else:
                print ('ERROR 404 : Invalid option')

    elif decision == 2:
        time.sleep(5)
        exit(0)
    else:
        print ('ERROR 404 : Invalid option')

def dungeon1_go():
    print 'esti sigur ca vrei sa merem la boss?'
    print '1. Da'
    print '2. Ne intoarcem la meniul principal'
    go = int(input(prompt))
    if go == 1:
        time.sleep(5)
        dungeon1()
    elif go == 2:
        time.sleep(5)
        main()
    else:
        print ('ERROR 404 : Invalid option')

def dungeon1():
    prompt = '> '
    player = random.randint(500,800)
    boss = random.randint(1000,3000)
    print 'Your Health %d' % player
    print 'Boss Health %d' % boss
    print 'Aici e un boss ce o sa faci ?'
    print '1. Pumn in coaie'
    print '2. RUN BITCH RUUUUUUN'
    decision = int(input(prompt))
    if decision == 1:
        while True:
            damage = random.randint(11,23)
            damage_boss = random.randint(500,800)
            time.sleep(0.5)
            print 'Vrei sa il ataci sau sa te retragi ?'
            print '1. Ataca'
            print '2. Retragete'
            ppwp = int(input(prompt))
            if ppwp == 1:
                print 'i-ai dat %d damage' % damage
                boss -= damage
                print 'ti-a dat %d damage' % damage_boss
                player -= damage_boss
                time.sleep(0.5)
                if boss < 10:
                    print 'ai batut boss-ul'
                    time.sleep(5)
                    main2()
                elif player <10:
                    print 'te-o facut ma'
                    time.sleep(5)
                    exit(0)
            elif ppwp == 2:
                time.sleep(5)
                exit(0)
    elif decision == 2:
        time.sleep(5)
        exit(0)
    else:
        print ('ERROR 404 : Invalid option')

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
                print 'Ce vrei sa facem?'
                print '1. Mergem La Boss'
                print '2. Mai incercam o data'
                wo = int(input(prompt))
                if wo == 1:
                    time.sleep(5)
                    dungeon1_go()
                elif wo == 2:
                    time.sleep(5)
                    search_wp()
                else:
                    print ('ERROR 404 : Invalid option')
            if fms >= 5:
                print 'fms-ul e +%d destul si rezistent cat sa bata un boss' % fms
                weapon = True
                time.sleep(5)
                main2()
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
        dungeon1()
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
