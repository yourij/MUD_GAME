import os
import time
import random
os.system('clear')
#________________________________MUD GAME________________________________

print('Welcome to MUD game.')

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
class NPC:
    def __init__(self, appearance, name, location, HP, immortal, isFound ) -> None:
        self.apperance = appearance # string, long description
        self.name = name            # string, short (Inkeeper, Princess, Witch...)
        # self.grid = grid            # list, XY coordinates (not used here)
        self.location = location    # TBA, inside or outside of house, trap etc. -> outside(default) / restaurant / castle / whichHut..
        self.HP = HP                # int, health points (0:100) where 0 = dead
        self.immortal = immortal    # boolean, if True = can not be dead
        self.isFound = isFound      # boolean, if True = visible to player and 'walks' with him (so maybe grid should be unlocked?)
class Player:
    def __init__(self, appearance, name, grid, location, HP, immortal, hpBonus ) -> None:
        self.apperance = appearance # string, long description
        self.name = name            # string, short (eg. default 'Player1' or anything)
        self.grid = grid            # list, XY coordinates
        self.location = location    # TBA, inside or outside of house, trap etc. -> outside(default) / restaurant / castle / whichHut..
        self.HP = HP                # int, health points (0:100) where 0 = dead
        self.immortal = immortal    # boolean, if True = can not be dead
        self.hpBonus = hpBonus      # int, eg. hpBonus=(-10) or hpBonus=20
class Item:
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
def talk():     # (future) talking with NPCs
    print('talk function')
def walk(input_direction):     # (IN PROGRESS...) moving aroung the grid
    print('walk function',playerPos[0])

    if (input_direction == 'N' or input_direction == 'n'):
        playerPos[1]+=1     # works ok, increasing the Y coordinate
        print('playerPos: ',playerPos,'grid: ',[currentPlace for currentPlace, currentGrid in gameFields.items() if currentGrid==playerPos])        # kurwa nie wiem jak ale to działa jeśli ==[1,1] / ale już currentGrid==playerPos troche mniej
        print('you moved North with use of walk()')
    elif (input_direction == 'S' or input_direction == 's'):
        playerPos[1]-=1
        print(playerPos)
        print('you moved South with use of walk()')
    elif (input_direction == 'E' or input_direction == 'e'):
        playerPos[0]+=1
        print(playerPos)
        print('you moved East with use of walk()')
    elif (input_direction == 'W' or input_direction == 'w'):
        playerPos[0]-=1
        print(playerPos)
        print('you moved West with use of walk()')    
    else:
        print('walk() says bye!')
def pickUp():   # (future) pick up an object function
    print('pickUp function')
def enter():    # (future) entering the buildings
    print('enter function')

# following should be moved to a separate file I guess... 
hillsDesc='Skaliste wzgórza wapienne, brak roślinności jeśli nie liczyć skąpych, na wpół uschniętych badyli wystających spośród skał'
riverValeyDesc='Dolina dzikiej rzeki. Wartki nurt z poszarpanymi brzegami. Zakole rzeki wyglądają na obiecujące łowisko.'
swampDesc='Bagna, bardzo niebezpieczne miejsce. Rzekłbym nawet, że dość wciągające... Wycofaj się albo...'
marschDesc='Mokradła, wilgotne i nieprzyjemne miejsce. Lepiej się tu nie zapuszczać, no chyba że się nie boisz.'
meadowDesc='Pełno tu pachnących ziół o odurzającym zapachu. Równinę przerzynają drogi białe i trochę zieleniejące od z rzadka porastającej je trawy;\n ku nim, niby strumienie ku rzekom, przybiegają z pól miedze, całe błękitne od bławatków, żółte od kamioły, różowe od dzięcieliny i smółek.\nZ obu stron każdej drogi szerokim pasem bieleją bujne rumianki i wyższe od nich kwiaty marchewnika, słają się w trawach fioletowe rohule, żółtymi gwiazdkami świecą brodawniki i kurze ślepoty.\nNienawidziłeś Orzeszkowej szczerze od dziecka. Do dziś na samo wspomnienie tego bełkotu zbiera Ci się na wymioty.'
dessertDesc='Pustynia, piaszczysta i nudna jak flaki z olejem. Z tym, że flaki z olejem zwykle nie występują na pustyni. No, chyba że ktoś zbyt długo na niej przebywa.'
thickForrestDesc='Gęsty las, mroczne miejsce. W sam raz dla wiedźm. Albo dzików. Albo uganiających się za nimi Galami. Rzymian nie stwierdzono.'
wildernessDesc='Las, gdzie dzikie zwierzęta czują się najlepiej. O na przykład takie, jak ten urodzy, półtonowy niedźwiedź stojący 20 metrów na prost... 15 metrów... 10 metrów... Serio? Dalej to czytasz?'
villageDesc='Wioska, po środku karczma. Krowa robi "Muuuu...".'
playerDesc='Mięśniak z kozikiem. Półmetrowej długości kozikiem.'
playerName='Stefan'
monsterDesc='Cuchnące bydlę. Tymczasowe, póki czegoś nie wymyślę cuchnące bydlę.'
monsterName='Arghargor, dla przyjaciół Pikuś'

# dict mapping the locations to grid system
gameFields={'hills'         :[0,0],              #   grid coordinates [x,y]
            'riverValey'    :[1,0],              #
            'swamp'         :[2,0],              #   [0,2]   [1,2]   [2,2]
            'marsch'        :[2,1],              #
            'meadow'        :[1,1],              #   [0,1]   [1,1]   [2,1]
            'dessert'       :[0,1],              #
            'thickForrest'  :[2,2],              #   [0,0]   [1,0]   [2,0]
            'wilderness'    :[1,2],              #
            'village'       :[0,2]               #   game starts in the middle [1,1]
            }

# class Field(...) instances
# instance_name = Field (0,     1,      2,    3,     4,                 5,              6                           )
# 0 = can go North from here (True/False)
# 1 = can go South from here (True/False)
# 2 = can go East from here (True/False)
# 3 = can go West from here (True/False)
# 4 = long text description to be printed each time player appears here
# 5 = instance short name, to be used somehow with walk() function to describe movement
# 6 = grid system
hills = Field           (True,  False, True,  False, hillsDesc,        'hills',        gameFields['hills']          )
riverValey = Field      (True,  False, True,  True,  riverValeyDesc,   'riverValey',   gameFields['riverValey']     )
swamp = Field           (True,  False, False, True,  swampDesc,        'swamp',        gameFields['swamp']          )
marsch = Field          (True,  True,  False, True,  marschDesc,       'marsch',       gameFields['marsch']         )
meadow = Field          (True,  True,  True,  True,  meadowDesc,       'meadow',       gameFields['meadow']         )   # GAME STARTS HERE!
dessert = Field         (True,  True,  True,  False, dessertDesc,      'dessert',      gameFields['dessert']        )
thickForrest = Field    (False, True,  False, True,  thickForrestDesc, 'thickForrest', gameFields['thickForrest']   )
wilderness = Field      (True,  True,  True,  True,  wildernessDesc,   'wilderness',   gameFields['wilderness']     )
village = Field         (True,  True,  True,  False, villageDesc,      'village',      gameFields['village']        )

sleepValue=.1                       # sleep value used in fight, when reprinting is done. May not be used in final game?
playerPos = gameFields['meadow']    # initial player position           
playerLoc = True                    # True - outside, False - entered any building
playerHP = 100                      # initial player health points.
playerImmortal = False              # DEFINE LATER OVERALL SYSTEM OF STATS MAINTENANCE AND PASSING
playerHPbonus = 10                  # initial player's attack bonus
monsterPos = [1,1]                  # TEMPORARY TEST MONSTER (POSITION)
monsterLoc = True                   # TEMPORARY TEST MONSTER (outside the building)
monsterHP = 100                     # TEMPORARY TEST MONSTER (health points), CHANGE THIS FOR FIGHTING TESTS 
monsterImmportal = False            # TEMPORARY TEST MONSTER (can be killed lock off if False) like before, this is for fight test only now
monsterHPbonus = 10                 # TEMPORARY TEST MONSTER (attack bonus), needs to be designed later
playerRand=random.randrange(10)     # random used for fighting tests
monsterRand=random.randrange(10)    # random used for fighting tests
# player 1 defined here (as well as dummy test monster)
player = Player (playerDesc, playerName, playerPos, playerLoc, playerHP, playerImmortal, playerHPbonus)
dummyMonster = Monster(monsterDesc, monsterName, monsterPos, monsterLoc, monsterHP, monsterImmportal, monsterHPbonus)

while (playerHP>0):
    # print('\n*** TEST ODCZYTU KIERUNKU ORAZ DZIAŁANIA KLASY FIELD ***\n')
    # print('Przybywasz na miejsce. '+meadowDesc)
    direction=input('Znajdujesz się na polu: '+str(playerPos)+', gdzie chcesz póść dalej? [N/S/E/W]: ')
    walk(direction)

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

    print("You are in:",playerPos,"right now.")

    print('\n\n')  


