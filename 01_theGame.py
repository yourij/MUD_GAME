import os
import time
import random
import fields 
# import functions (later all fights etc to be moved there)
os.system('clear')
#________________________________MUD GAME________________________________
print('Welcome to MUD game.\n')
print('''
LEGEND:
N = idź na północ
S = idź na południe
E = idź na wschód
W = idź na zachód
L = rozejrzyj się
T = rozmawiaj
F = walcz (future)
H = wyświetl pomoc
''')


# TO DO LIST
# 1) Create parent-child class system instead of following simple classes
# 2) ...and more :)
class Field:
    def __init__(self, North, South, East, West, appearance, name, grid) -> None:
        self.North = North          # boolean
        self.South = South          # boolean
        self.East = East            # boolean
        self.West = West            # boolean
        self.apperance = appearance # string, long description
        self.name = name            # string, short
        self.grid = grid            # list, XY coordinates - in case of Field maybe tuple instead of list?
class Place:
    def __init__(self, appearance, name, location, isLocked) -> None:
        self.apperance = appearance # string, long description
        self.name = name            # string, short (Inkeeper, Princess, Witch...)
        self.location = location    # TBA, inside or outside of house, trap etc. -> outside(default) / restaurant / castle / whichHut..
        self.isLocked = isLocked    # boolean, isLocked = True - player can not enter inside (trap used/broken, castle with no key etc.)
class Npc:
    def __init__(self, appearance, name, location, HP, immortal, isFound ) -> None:
        self.apperance = appearance # string, long description
        self.name = name            # string, short (Inkeeper, Princess, Witch...)
        # self.grid = grid            # list, XY coordinates (not used here)
        self.location = location    # TBA, inside or outside of house, trap etc. -> outside(default) / restaurant / castle / whichHut..
        self.HP = HP                # int, health points (0:100) where 0 = dead
        self.immortal = immortal    # boolean, if True = can not be dead
        self.isFound = isFound      # boolean, if True = visible to player and 'walks' with him (so maybe grid should be unlocked?)
class Player:   # used in fight(), not used (yet) in walk()
    def __init__(self, appearance, name, grid, location, HP, immortal, hpBonus ) -> None:
        self.apperance = appearance # string, long description
        self.name = name            # string, short (eg. default 'Player1' or anything)
        self.grid = grid            # list, XY coordinates
        self.location = location    # TBA, inside or outside of house, trap etc. -> outside(default) / restaurant / castle / whichHut..
        self.HP = HP                # int, health points (0:100) where 0 = dead
        self.immortal = immortal    # boolean, if True = can not be dead
        self.hpBonus = hpBonus      # int, eg. hpBonus=(-10) or hpBonus=20
class Item: # currently hiddenKey that player has to find
    def __init__(self, appearance, name, grid, location, isFound) -> None:
        self.apperance = appearance # string, long description
        self.name = name            # string, short (Inkeeper, Princess, Witch...)
        self.grid = grid            # list, XY coordinates
        self.location = location    # TBA, inside or outside of house, trap etc. -> outside(default) / restaurant / castle / whichHut..
        self.isFound = isFound      # boolean, if True = visible to player and 'walks' with him (so maybe grid should be unlocked?)
class Food:
    def __init__(self, appearance, name, location, hpBonus) -> None:
        self.apperance = appearance # string, long description
        self.name = name            # string, short (eg. default 'Player1' or anything)
        self.location = location    # TBA, inside or outside of house, trap etc. -> outside(default) / restaurant / castle / whichHut..
        self.hpBonus = hpBonus      # int, eg. hpBonus=(-10) or hpBonus=20
class Monster:
    def __init__(self, appearance, name, grid, location, HP, immortal, hpBonus) -> None:
        self.apperance = appearance # string, long description
        self.name = name            # string, short (eg. default 'Player1' or anything)
        self.grid = grid            # list, XY coordinates
        self.location = location    # TBA, inside or outside of house, trap etc. -> outside(default) / restaurant / castle / whichHut..
        self.HP = HP                # int, health points (0:100) where 0 = dead
        self.immortal = immortal    # boolean, if True = can not be dead
        self.hpBonus = hpBonus      # int, eg. hpBonus=(-10) or hpBonus=20

# TO DO LIST (fight):
# 1) clear function - passing HP after is done, sleep value and clear are ok, remove trash if any
# 2) random HP bonus should be random before each fight - so should be included in function, not in main code.
# 3) future - random should be applied to HP bonus as well
def fight(PlayerHP,OpponentHP, PlayerHPbonus, OpponentHPbonus,playerRand, opponentRand): #    passing: playerHP,playerHPbonus, monsterHP, monsterHPbonus - OpponentHP locally as it not always be fight with a monster!
    PlayerHP=PlayerHP+playerRand
    OpponentHP=OpponentHP+opponentRand
    print('fight function')
    print('\nRunda 1. Ty: ',PlayerHP,' vs przeciwnik: ',OpponentHP)
    # TO DO LIST
    # 1) randomly generated starting player function here, as for now Player starts always: OpponentHP=OpponentHP-PlayerHPbonus
    # 2) player hit bonus luck = % of chance of the 2nd hit during his round
    while (PlayerHP > 0) and (OpponentHP > 0):
        os.system('clear')  # this should be removed later, it is OK only for testing
        print('\nTy: ',PlayerHP,' vs przeciwnik: ',OpponentHP,' rand bonus: ',playerRand,'vs ', opponentRand)
        time.sleep(sleepValue)
        print('\nZadajesz cios, przeciwnik traci: ',PlayerHPbonus,'\n')
        time.sleep(sleepValue)
        OpponentHP=OpponentHP-PlayerHPbonus
        if (OpponentHP>0):
            PlayerHP = (PlayerHP)-OpponentHPbonus
            print('Przeciwnik uderza, tracisz: ',OpponentHPbonus)
            time.sleep(sleepValue*2)     
    print("KONIEC WALKI")
    
    if (PlayerHP > OpponentHP):
        result=PlayerHP-OpponentHP
        print('Zostało Ci :'+str(PlayerHP)+' HP')
    elif (PlayerHP < OpponentHP):
        result=0                        # HP=0, Player dies
        print('Zostało Ci :'+str(PlayerHP)+' HP')
        print('Umierasz na śmierć...')
    else:
        print("Mierzycie się wzrokiem ale żaden z was nie odważy się na nic więcej...")
        result=PlayerHP
    return(result)                      # result gives new HP for player
def talk(input):     # (future) talking with NPCs
    if (playerPos == witchPos):
        print(' - Czego chcesz, nieznajomy? Chcesz jabłuszko?')
    elif (playerPos == innKeeperPos):
        print(' - Co podać?')
    elif (playerPos == princessPos):
        print(' - Przybyłeś mnie uratować? No spoko, tylko wiesz... kratę otwórz.')
    else:
        print('...Sam ze sobą możesz najwyżej pogadać...')
# TO DO LIST (walk):
# 1) use retrieved key from gameFields{} to present on screen
# 2) define something more useful in else: for bad user input
# 3) question - to be checked. Currently it does not return anything as playerPos is global variable... is it ok like this?
def walk(input_direction):     # moving aroung the grid, gets input from user (north-south-east-west direction)
    # print('declared movement input: ',input_direction)
    # print('playerPos at start of walk()',playerPos)
    # reads the current position to check where can player go:
    current_grid=[currentPlace for currentPlace, currentGrid in gameFields.items() if currentGrid==playerPos] # searching values in dict:gameFields{} to get the key (field name) 
    # print("Before the movement: ",current_grid)
    if ((input_direction == 'N' or input_direction == 'n')):
        time.sleep(sleepValue)
        if playerPos[1]==2:
            print('KONIEC MAPY !!!!!!')
        else:
            playerPos[1]=playerPos[1]+1     # increase the Y coordinate by 1
            time.sleep(sleepValue)  
            print('Kierujesz się na północ...')
    elif (input_direction == 'S' or input_direction == 's'):
        time.sleep(sleepValue)
        if playerPos[1]==0:
            print('KONIEC MAPY !!!!!!')
        else:
            playerPos[1]=playerPos[1]-1 # decrease the Y coordinate by 1
            time.sleep(sleepValue)
            print('Kierujesz się na południe...')
    elif (input_direction == 'E' or input_direction == 'e'):
        time.sleep(sleepValue)
        if playerPos[0]==2:
            print('KONIEC MAPY !!!!!!')
        else:
            playerPos[0]=playerPos[0]+1 # increase the X coordinate by 1
            time.sleep(sleepValue)
            print('Kierujesz się na wschód...')
    elif (input_direction == 'W' or input_direction == 'w'):
        time.sleep(sleepValue)
        if playerPos[0]==0:
            print('KONIEC MAPY !!!!!!')
        else:
            playerPos[0]=playerPos[0]-1 # decrease the X coordinate by 1
            time.sleep(sleepValue)
            print('Kierujesz się na zachód...')    
    else:
        print('Ech... Wciśnij "N", jeśli chcesz iść na północ, "S" gdy na południe, "W" poprowadzi Cię na zachód, "E" prowadzi Cię na wchód')
    if (playerPos==witchPos):
        print('Spotykasz wiedźmę')
    elif (playerPos==innKeeperPos):
        print('Spotykasz karczmarza')
    elif (playerPos==princessPos):
        print('Spotykasz księżniczkę')
    else:
        print('Jesteś tu sam.')
    time.sleep(sleepValue)
    current_grid=[currentPlace for currentPlace, currentGrid in gameFields.items() if currentGrid==playerPos]
    return(current_grid)
def pickUp():   # (future) pick up an object function
    print('pickUp function')
def enter():    # (future) entering the buildings
    print('enter function')

# player
playerName='Stefan'
playerDesc='Mięśniak z kozikiem. Półmetrowej długości kozikiem.'
playerPos = [1,1]                   # initial player position [x,y]. It must be a list with direct values
playerLoc = True                    # True - outside, False - entered any building
playerHP = 100                      # initial player health points.
playerImmortal = False              # DEFINE LATER OVERALL SYSTEM OF STATS MAINTENANCE AND PASSING
playerHPbonus = 10                  # initial player's attack bonus
playerRand=random.randrange(10)     # random used for fighting tests
# hidden key
hiddenKeyName='Kluczyk'
hiddenKeyDesc='Klucz jak klucz. Dobry do lania wosku'
hiddenKeyPos = [1,2]                # key initial location on grid, must be direct value
hiddenKeyLoc = False                # initial location=False means its inside a building (like inside a witch's hut)
hiddenKeyFound = False              # initial value = False (player does not even see it). If =True means player has found it and may keep it and use it.
# witch
witchName='Wiedźma'
witchDesc='Niby stara baba ale dość żywotna. Może ma pakiet multisporta z Gildii Wiedźm?'
witchPos = [2,2]
witchHP = 100
witchFound = True   # if False = she is gone, no acton possible. Try next time you visit her.
# princess
princessName='Księżniczka'
princessDesc='Dwie nogi, dwie ręce, głowa... tylko wszystko jakieś takie... Przepiękne.'
princessPos = [0,0]
princessHP = 1
princessFound = False   # if False... well.. I dunno, maybe she went to a toilet? This to be done later
# innKeeper
innKeeperName='Karczmarz'
innKeeperDesc='Gruby jak bela, fartuch poplamiony sosem'
innKeeperPos = [0,2]
innKeeperHP = 100
innKeeperFound = True   # if False, he went to sleep and no food is served
# dummy Monster
monsterName='Arghargor, dla przyjaciół Pikuś'
monsterDesc='Cuchnące bydlę. Tymczasowe, póki czegoś nie wymyślę cuchnące bydlę.'
monsterPos = [1,1]                  # TEMPORARY TEST MONSTER (POSITION)
monsterLoc = True                   # TEMPORARY TEST MONSTER (outside the building)
monsterHP = 100                     # TEMPORARY TEST MONSTER (health points), CHANGE THIS FOR FIGHTING TESTS 
monsterImmportal = False            # TEMPORARY TEST MONSTER (can be killed lock off if False) like before, this is for fight test only now
monsterHPbonus = 10                 # TEMPORARY TEST MONSTER (attack bonus), needs to be designed later
monsterRand=random.randrange(10)    # random used for fighting tests
# not-object specific values
sleepValue=.5                       # sleep value used in fight, when reprinting is done. May not be used in final game?
can_be_killed = True                # optional (see playerImmportal and similair)
can_not_be_killed = True            # optional (see playerImmportal and similair)

# dict mapping the locations to grid system
gameFields ={'hills'                :[0,0],             #   grid coordinates [x,y]
             'riverValey'           :[1,0],             #
             'swamp'                :[2,0],             #   [0,2]   [1,2]   [2,2]
             'marsh'                :[2,1],             #
             'meadow'               :[1,1],             #   [0,1]   [1,1]   [2,1]
             'dessert'              :[0,1],             #
             'thickForrest'         :[2,2],             #   [0,0]   [1,0]   [2,0]
             'wilderness'           :[1,2],             #
             'village'              :[0,2]              #   game starts in the middle [1,1]
            }
# dict mapping the field descriptions to grid system
gameFieldsDesc={ fields.hillsDescription()          :[0,0],             #
                 fields.riverValeyDescription()     :[1,0],             #
                 fields.swampDescription()          :[2,0],             #
                 fields.marshDescription()          :[2,1],             #
                 fields.meadowDescription()         :[1,1],             #
                 fields.dessertDescription()        :[0,1],             #
                 fields.thickForrestDescription()   :[2,2],             #
                 fields.wildernessDescription()     :[1,2],             #
                 fields.villageDescription()        :[0,2]              #
            }

# class Field(...) instances
# instance_name = Field (0,1,2,3,4,5,6)
# 0:3 = can go North/South/East/West from here (True/False)
# 4   = long text description to be printed each time player appears here
# 5   = instance short name, to be used somehow with walk() function to describe movement
# 6   = grid system
hills = Field       (True, False,True, False,gameFieldsDesc[fields.hillsDescription()],       'hills',       gameFields['hills']       )
riverValey = Field  (True, False,True, True, gameFieldsDesc[fields.riverValeyDescription()],  'riverValey',  gameFields['riverValey']  )
swamp = Field       (True, False,False,True, gameFieldsDesc[fields.swampDescription()],       'swamp',       gameFields['swamp']       )
marsh = Field       (True, True, False,True, gameFieldsDesc[fields.marshDescription()],       'marsh',       gameFields['marsh']       )
meadow = Field      (True, True, True, True, gameFieldsDesc[fields.meadowDescription()],      'meadow',      gameFields['meadow']      ) # GAME STARTS HERE!
dessert = Field     (True, True, True, False,gameFieldsDesc[fields.dessertDescription()],     'dessert',     gameFields['dessert']     )
thickForrest = Field(False,True, False,True, gameFieldsDesc[fields.thickForrestDescription()],'thickForrest',gameFields['thickForrest'])
wilderness = Field  (True, True, True, True, gameFieldsDesc[fields.wildernessDescription()],  'wilderness',  gameFields['wilderness']  )
village = Field     (True, True, True, False,gameFieldsDesc[fields.villageDescription()],     'village',     gameFields['village']     )


# Player, NPCs, Monsters and other Objects appearing in the game definition here:
player      = Player(playerDesc,playerName,playerPos,playerLoc,playerHP,playerImmortal,playerHPbonus)
hiddenKey   = Item(hiddenKeyDesc,hiddenKeyName,hiddenKeyPos,hiddenKeyLoc,hiddenKeyFound)
witch       = Npc(witchDesc,        witchName,      witchPos,       witchHP,        can_be_killed,    witchFound )
princess    = Npc(princessDesc,     princessName,   princessPos,    princessHP,     can_not_be_killed,princessFound )
innKeeper   = Npc(innKeeperDesc,    innKeeperName,  innKeeperPos,   innKeeperHP,    can_not_be_killed,innKeeperFound )
# dummy to be removed later
dummyMonster = Monster(monsterDesc, monsterName, monsterPos, monsterLoc, monsterHP, monsterImmportal, monsterHPbonus)

print('Przybywasz na miejsce. '+fields.meadowDescription()+'\n')    # CHANGE THIS if starting position is changed. Otherwise its a direct callout of field description
while (playerHP>0):
    show_grid=[current_Place for current_Place, current_Grid in gameFields.items() if current_Grid==playerPos]
    u_inp=input('Znajdujesz się na polu: '+str(player.grid)+' '+str(show_grid)+'.Podaj komendę\n (N) (S) (E) (W) (T) (L) (H) (F)? ')
    # make this OR thing shorter somehow !!!
    if (u_inp=='N' or u_inp=='n' or u_inp=='S' or u_inp=='s' or u_inp=='E' or u_inp=='e' or u_inp=='W' or u_inp=='w'):
            walk_result=walk(u_inp)
    elif ((u_inp=='T' or u_inp=='t')):
        talk(u_inp)
    elif ((u_inp=='L' or u_inp=='l')):
        show_desc=[x for x, current_Desc in gameFieldsDesc.items() if current_Desc==playerPos]
        print(str(show_desc[0]))
    elif ((u_inp=='F' or u_inp=='f')):
        print('\n - Walka nie gotowa, muszę napisać utworzyć potwory i skończyć system walki.')
        print('...odezwał się jakiś głos wewnątrz Twojej głowy.')
    elif ((u_inp=='H' or u_inp=='h')):
        print('''
            LEGEND_:
            N = idź na północ
            S = idź na południe
            E = idź na wschód
            W = idź na zachód
            L = rozejrzyj się
            T = rozmawiaj
            F = walcz (future)
            H = wyświetl pomoc
            ''')
    else:
        print('USE YOU KEYBOARD WISELY...')

    

    # print('\n')  
    # print('\n*** TEST SYSTEMU WALKI (on hold, seems to work***\n')
    # print('Walka pomiędzy',player.name,'oraz', dummyMonster.name)
    # print('Masz obecnie',playerHP,'a Twój przeciwnik',monsterHP)
    # playerHP=fight(playerHP, monsterHP, playerHPbonus, monsterHPbonus, playerRand, monsterRand)
    # print('\n\nTest przekazania HP po walce do statystyk gracza')
    # print('playerHP=',playerHP)
    # print('Walka numer 2')
    # playerHP=fight(playerHP, monsterHP, playerHPbonus, monsterHPbonus, playerRand, monsterRand)
    # print("\nRessurection xD")

    # print("You are in:",playerPos,"right now.")     # calling directly playerPos variable works fine
    # print("Player instance location: ",player.grid) # calling player.grid works fine as well

    # print('\n')  


