import os
os.system('clear')
#________________________________MUD GAME________________________________

print('Welcome to MUD game.')


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
    def __init__(self, appearance, name, grid, location, HP, immortal ) -> None:
        self.apperance = appearance # string, long description
        self.name = name            # string, short (eg. default 'Player1' or anything)
        self.grid = grid            # list, XY coordinates
        self.location = location    # TBA, inside or outside of house, trap etc. -> outside(default) / restaurant / castle / whichHut..
        self.HP = HP                # int, health points (0:100) where 0 = dead
        self.immortal = immortal    # boolean, if True = can not be dead
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

def fight(PlayerHP,OpponentHP):
    print('fight function')
    print(PlayerHP,' vs ',OpponentHP)
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

hillsDesc='Skaliste wzgórza wapienne'
riverValeyDesc='Dolina dzikiej rzeki'
swampDesc='Bagna, bardzo niebezpieczne miejsce'
marschDesc='Mokradła, wilgotne i nieprzyjemne miejsce'
meadowDesc='Łąka, słoneczna i zielona'
dessertDesc='Pustynia, piaszczysta i nudna jak flaki z olejem'
thickForrestDesc='Gęsty las, mroczne miejsce. W sam raz dla wiedźm.'
wildernessDesc='Las, gdzie dzikie zwierzęta czują się najlepiej'
villageDesc='Wioska, po środku karczma. Krowa robi "Muuuu...".'
playerDesc='Mięśniak z kozikiem'
playerName='Stefan'
monsterDesc='Cuchnące bydlę'
monsterName='Arghargor'

hills = Field           (True,  False, True,  False, hillsDesc,        'hills',        [0,0])
riverValey = Field      (True,  False, True,  True,  riverValeyDesc,   'riverValey',   [1,0])
swamp = Field           (True,  False, False, True,  swampDesc,        'swamp',        [2,0])
marsch = Field          (True,  True,  False, True,  marschDesc,       'marsch',       [2,1])
meadow = Field          (True,  True,  True,  True,  meadowDesc,       'meadow',       [1,1])   # GAME STARTS HERE!
dessert = Field         (True,  True,  True,  False, dessertDesc,      'dessert',      [0,1])
thickForrest = Field    (False, True,  False, True,  thickForrestDesc, 'thickForrest', [2,2])
wilderness = Field      (True,  True,  True,  True,  wildernessDesc,   'wilderness',   [1,2])
village = Field         (True,  True,  True,  False, villageDesc,      'village',      [0,2])

playerPos = [1,1]
playerLoc = True            # True - outside, False - entered any building
playerHP = 100
playerImmortal = False      # DEFINE LATER OVERALL SYSTEM OF STATS MAINTENANCE AND PASSING
monsterPos = [1,1]
monsterLoc = True
monsterHP = 99              # ------------> CHANGE THIS FOR FIGHTING TESTS <--------------
monsterImmportal = False    # like before, this is for fight test only now
monsterHPbonus = 20         # whatever, needs to be designed later



player = Player (playerDesc, playerName, playerPos, playerLoc, playerHP, playerImmortal)
dummyMonster = Monster(monsterDesc, monsterName, monsterPos, monsterLoc, monsterHP, monsterImmportal, monsterHPbonus)



print('\n*** TEST ODCZYTU KIERUNKU ORAZ DZIAŁANIA KLASY FIELD ***\n')
print('Przybywasz na miejsce. Przed Tobą '+meadow.apperance.lower())
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

print('\n\n')  


