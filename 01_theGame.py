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
        os.system('clear')
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
def talk():
    print('talk function')
def walk():
    print('walk function')
def pickUp():
    print('pickUp function')
def enter():
    print('enter function')

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

hills = Field           (True,  False, True,  False, hillsDesc,        'hills',        [0,0])
riverValey = Field      (True,  False, True,  True,  riverValeyDesc,   'riverValey',   [1,0])
swamp = Field           (True,  False, False, True,  swampDesc,        'swamp',        [2,0])
marsch = Field          (True,  True,  False, True,  marschDesc,       'marsch',       [2,1])
meadow = Field          (True,  True,  True,  True,  meadowDesc,       'meadow',       [1,1])   # GAME STARTS HERE!
dessert = Field         (True,  True,  True,  False, dessertDesc,      'dessert',      [0,1])
thickForrest = Field    (False, True,  False, True,  thickForrestDesc, 'thickForrest', [2,2])
wilderness = Field      (True,  True,  True,  True,  wildernessDesc,   'wilderness',   [1,2])
village = Field         (True,  True,  True,  False, villageDesc,      'village',      [0,2])

sleepValue=.1
playerPos = [1,1]
playerLoc = True            # True - outside, False - entered any building
playerHP = 100
playerImmortal = False      # DEFINE LATER OVERALL SYSTEM OF STATS MAINTENANCE AND PASSING
playerHPbonus = 10
monsterPos = [1,1]
monsterLoc = True
monsterHP = 100              # ------------> CHANGE THIS FOR FIGHTING TESTS <--------------
monsterImmportal = False    # like before, this is for fight test only now
monsterHPbonus = 10         # whatever, needs to be designed later
playerRand=random.randrange(10)
monsterRand=random.randrange(10)

player = Player (playerDesc, playerName, playerPos, playerLoc, playerHP, playerImmortal, playerHPbonus)
dummyMonster = Monster(monsterDesc, monsterName, monsterPos, monsterLoc, monsterHP, monsterImmportal, monsterHPbonus)



print('\n*** TEST ODCZYTU KIERUNKU ORAZ DZIAŁANIA KLASY FIELD ***\n')
print('Przybywasz na miejsce. '+meadowDesc)
direction=input('Gdzie chcesz póść dalej? [N/S/E/W] ')

if (direction == 'N' or direction == 'n'):
    print('North')
elif (direction == 'S' or direction == 's'):
    print('South')
elif (direction == 'E' or direction == 'e'):
    print('East')
elif (direction == 'W' or direction == 'w'):
    print('West')    
else:
    print('bye!')
print('\n')  
print('\n*** TEST SYSTEMU WALKI ***\n')
print('Walka pomiędzy',player.name,'oraz', dummyMonster.name)
print('Masz obecnie',playerHP,'a Twój przeciwnik',monsterHP)

playerHP=fight(playerHP, monsterHP, playerHPbonus, monsterHPbonus, playerRand, monsterRand)
print('\n\nTest przekazania HP po walce do statystyk gracza')
print('playerHP=',playerHP)
print('Walka numer 2')
playerHP=fight(playerHP, monsterHP, playerHPbonus, monsterHPbonus, playerRand, monsterRand)

print('\n\n')  


