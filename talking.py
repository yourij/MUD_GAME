import random
import sys
import time
import json
sleepValue=1

def phrase_look():          # future to make code more compact
    pass

def talk(playerPos, witchPos, innKeeperPos, princessPos, hiddenKeyFound):     # talking with NPCs
    with open('talking.json') as f:
       my_json = json.load(f)
    f.close()
#____________INNKEEPER____________
    inn_hello = '''
 - Co podać? Tu jest menu (M):
(P) - Zupa pomidorowa : 1 oko wiedźmy
(R) - Rosół           : 2 oczy wiedźmy
(Z) - Żurek           : 3 oczy wiedźmy 
'''
    inn_dish1 = '\n - Proszę, pomidorowa jak chciałeś.'
    inn_dish2 = '\n - Rosół z kur dużej ilości, wedle życzenia'
    inn_dish3 = '\n - Żurek z jajeczkiem, nasza specjalność!'
    inn_menu = '''\n - Podałem już menu (M):
(P) - Zupa pomidorowa : 1 oko wiedźmy
(R) - Rosół           : 2 oczy wiedźmy
(Z) - Żurek           : 3 oczy wiedźmy 
'''
    inn_repeat = '\n - Co tam panie, bełkoczesz?\n'
#____________WITCH____________
    witch_math_quest = {
        '1x1': '1',  '1x2': '2',  '1x3': '3',  '1x4': '4',  '1x5': '5',  '1x6': '6',  '1x7': '7',  '1x8': '8',  '1x9': '9',  '1x10': '10',
        '2x1': '2',  '2x2': '4',  '2x3': '6',  '2x4': '8',  '2x5': '10',  '2x6': '12',  '2x7': '14',  '2x8': '16',  '2x9': '18',  '2x10': '20',
        '3x1': '3',  '3x2': '6',  '3x3': '9',  '3x4': '12',  '3x5': '15',  '3x6': '18',  '3x7': '21',  '3x8': '24',  '3x9': '27',  '3x10': '30',
        '4x1': '4',  '4x2': '8',  '4x3': '12',  '4x4': '16',  '4x5': '20',  '4x6': '24',  '4x7': '28',  '4x8': '32',  '4x9': '36',  '4x10': '40',
        '5x1': '5',  '5x2': '10',  '5x3': '15',  '5x4': '20',  '5x5': '25',  '5x6': '30',  '5x7': '35',  '5x8': '40',  '5x9': '45',  '5x10': '50',
        '6x1': '6',  '6x2': '12',  '6x3': '18',  '6x4': '24',  '6x5': '30',  '6x6': '36',  '6x7': '42',  '6x8': '48',  '6x9': '54',  '6x10': '60',
        '7x1': '7',  '7x2': '14',  '7x3': '21',  '7x4': '28',  '7x5': '35',  '7x6': '42',  '7x7': '49',  '7x8': '56',  '7x9': '63',  '7x10': '70',
        '8x1': '8',  '8x2': '16',  '8x3': '24',  '8x4': '32',  '8x5': '40',  '8x6': '48',  '8x7': '56',  '8x8': '64',  '8x9': '72',  '8x10': '80',
        '9x1': '9',  '9x2': '18',  '9x3': '27',  '9x4': '36',  '9x5': '45',  '9x6': '54',  '9x7': '63',  '9x8': '72',  '9x9': '81',  '9x10': '90',
        '10x1':'10',  '10x2': '20',  '10x3': '30',  '10x4': '40',  '10x5': '50',  '10x6': '60',  '10x7': '70',  '10x8': '80',  '10x9': '90',  '10x10': '100'
    }
    random_math_question=random.choice(list(witch_math_quest.keys()))
    witch_hello = '\n - Czego chcesz, nieznajomy? Chcesz jabłuszko? (T/N): '
    witch_gives_apple = '\n - Smacznego, hahaha... A teraz już idź, nic więcej dla Ciebie nie mam.'
    witch_asking_1 = '\n - Nie jesteś głodny? Czy chcesz coś jeszcze? (T/N): '
    witch_math = '\n - No dobrze, dam Ci coś jeśli powiesz, ile to jest '+str(random_math_question)+': '
    witch_gives_award = '\n - DOSKONALE! Widać, że znasz tabliczkę mnożenia! Weź proszę ten KLUCZ. :)\n'
    witch_gives_no_award = '\n - No chyba sobie żartujesz! Wróć, gdy się dowiesz ile to jest!\n'
    witch_response_key1 = '\n - Aaa... mam go od dawna, ale jestem tak stara...'
    witch_response_key2 = 'Poszukaj w okolicy, może we wiosce? - dodaje wiedźma po chwili.'
    witch_goodbye1 = '\n - Do widzenia!\n'
    witch_goodbye2 = '\n - Nie wiem, o czym mówisz. Jestem zajęta, przyjdź kiedy indziej\n'
#____________PLAYER____________
    player_gets_key = 'Bierzesz do ręki zardzewiały klucz.'
    player_responds_key = '\n - A możesz mi... Może Pani powiedzieć, do czego ten klucz?'

#____________PRINCESS____________
    princess_hello_locked = ' - Przybyłeś mnie uratować? No spoko, tylko wiesz... kratę otwórz.'
    princess_hello_unlocked = ' - Powiedz, że potrafisz pozbyć się tej kraty. Och, tyle czasu już tu siedzę zamknięta... Buuu.... \nW tym momencie księżniczka rozpłakała się na dobre.'
    princess_reacts_gate_opens = ' - Cudownie, w końcu wolność. Otwieraj szybciej, już nie mogę się doczekać!' 
    princess_reacts_gate_closed = ' - Jak to? Myślałam, że udało Ci się zdobyć klucz. Wróć proszę z kluczem!'
    princess_open_gate_decide = ' - Masz klucz do kłódki w kracie? (T/N): '

    princess_row01 = '                 __'
    princess_row02 = '                /__`.'
    princess_row03 = '               / \ `\ \ '
    princess_row04 = '              /   \  `\ '
    princess_row05 = '             /     \   \ '
    princess_row06 = '            /_______\  /\ '
    princess_row07 = '            (((( ))))'
    princess_row08 = "           (((' . ')))"
    princess_row09 = '           (((\_-_/)))'
    princess_row10 = '           (((_) (_)))'
    princess_row11 = '          /((( \ / )))\ '
    princess_row12 = '         / (((  ^  ))) \ '
    princess_row13 = '        / / ((  ^  )) \ \ '
    princess_row14 = '       ( (   \  ^  /   ) )'
    princess_row15 = '        \ \   )www(   / /'
    princess_row16 = "         `\\ /     \ //'"
    princess_row17 = "           /'       `\ "
    princess_row18 = '          /           \ '
    princess_row19 = '         /             \ '
    princess_row20 = '        /               \ '
    princess_row21 = '       /                 \ '
    princess_row22 = '      /                   \ '
    princess_row23 = '     /                     \ '
    princess_row24 = '    /                       \ '
    princess_row25 = '   /                         \ '
    princess_row26 = '  /                           \ '
    princess_row27 = ' |                             |'
    princess_row28 = "  `-----......_____......-----'"
    princess_row29 = '                               '

 #____________talking____________   
    if (playerPos == witchPos):
        with open('talking.json') as f:
            my_json = json.load(f)
        for phrase in my_json["phrases"]:
            u_inp=input(phrase["witch_hello"])
        if (u_inp=='T' or u_inp=='t'):
            for phrase in my_json["phrases"]:
                print(phrase["witch_gives_apple"])
        elif (u_inp=='N' or u_inp=='n'):
            for phrase in my_json["phrases"]:
                u_inp=input(phrase["witch_asking_1"])
            if (u_inp=='T' or u_inp=='t'):
                # witch_math_quest[random_math_question]
                u_inp=input(witch_math)                       # not a JSON because of '+str(random_math_question)+'
                if (u_inp==witch_math_quest[random_math_question]):
                    hiddenKeyFound=True
                    for phrase in my_json["phrases"]:
                        print(phrase["witch_gives_award"])
                    time.sleep(sleepValue)
                    for phrase in my_json["phrases"]:
                        print(phrase["player_gets_key"])
                    time.sleep(sleepValue)
                    for phrase in my_json["phrases"]:
                        print(phrase["player_responds_key"])
                    time.sleep(sleepValue)
                    for phrase in my_json["phrases"]:
                        print(phrase["witch_response_key1"])
                    time.sleep(sleepValue)
                    for phrase in my_json["phrases"]:
                        print(phrase["witch_response_key2"])
                    time.sleep(sleepValue)
                    for phrase in my_json["phrases"]:
                        print(phrase["witch_goodbye1"])
                    time.sleep(sleepValue)
                else:
                    for phrase in my_json["phrases"]:
                        print(phrase["witch_gives_no_award"])
            elif (u_inp=='N' or u_inp=='n'):
                for phrase in my_json["phrases"]:
                    print(phrase["witch_goodbye1"])            
            else:
                for phrase in my_json["phrases"]:
                    print(phrase["witch_goodbye2"])
        else:
            for phrase in my_json["phrases"]:
                print(phrase["witch_goodbye2"])
            
    elif (playerPos == innKeeperPos):
        u_inp=input(inn_hello)
        if (u_inp=='P' or u_inp=='p'):
            print(inn_dish1)
        elif (u_inp=='R' or u_inp=='r'):
            print(inn_dish2)
        elif (u_inp=='Z' or u_inp=='z'):
            print(inn_dish3)
        elif (u_inp=='M'):
            print(inn_menu)
        else:
            print(inn_repeat)

    elif (playerPos == princessPos):
        if (hiddenKeyFound==False or hiddenKeyFound==None):     # how to force the game not to switch into None?
            print(princess_hello_locked)
        elif (hiddenKeyFound==True):
            print(princess_hello_unlocked)
            u_inp=input(princess_open_gate_decide)
            if (u_inp=='T' or u_inp=='t'):
                print(princess_reacts_gate_opens)
                print('\n\n\n')
                print(princess_row01)
                time.sleep(sleepValue/2)
                print(princess_row02)
                time.sleep(sleepValue/2)
                print(princess_row03)
                time.sleep(sleepValue/2)
                print(princess_row04)
                time.sleep(sleepValue/2)
                print(princess_row05)
                time.sleep(sleepValue/2)
                print(princess_row06)
                time.sleep(sleepValue/2)
                print(princess_row07)
                time.sleep(sleepValue/2)
                print(princess_row08)
                time.sleep(sleepValue/2)
                print(princess_row09)
                time.sleep(sleepValue/2)
                print(princess_row10)
                time.sleep(sleepValue/2)
                print(princess_row11)
                time.sleep(sleepValue/2)
                print(princess_row12)
                time.sleep(sleepValue/2)
                print(princess_row13)
                time.sleep(sleepValue/2)
                print(princess_row14)
                time.sleep(sleepValue/2)
                print(princess_row15)
                time.sleep(sleepValue/2)
                print(princess_row16)
                time.sleep(sleepValue/2)
                print(princess_row17)
                time.sleep(sleepValue/2)
                print(princess_row18)
                time.sleep(sleepValue/2)
                print(princess_row19)
                time.sleep(sleepValue/2)
                print(princess_row20)
                time.sleep(sleepValue/2)
                print(princess_row21)
                time.sleep(sleepValue/2)
                print(princess_row22)
                time.sleep(sleepValue/2)
                print(princess_row23)
                time.sleep(sleepValue/2)
                print(princess_row24)
                time.sleep(sleepValue/2)
                print(princess_row25)
                time.sleep(sleepValue/2)
                print(princess_row26)
                time.sleep(sleepValue/2)
                print(princess_row27)
                time.sleep(sleepValue/2)
                print(princess_row28)
                time.sleep(sleepValue/2)
                print(princess_row29)
                time.sleep(sleepValue/2)
                print('GRATULACJE - WYGRAŁEŚ GRĘ!\n\n\n')
                sys.exit()
            else:
                print(princess_reacts_gate_closed)
    else:
        print('...Sam ze sobą możesz najwyżej pogadać...')
# hiddenKeyFound=True
#    f.close()
    return(hiddenKeyFound)