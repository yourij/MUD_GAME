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
        self.grid = grid            # list, XY coordinates

hillsDesc='Skaliste wzgórza wapienne'
riverValeyDesc='Dolina dzikiej rzeki'
swampDesc='Bagna, bardzo niebezpieczne miejsce'
marschDesc='Mokradła, wilgotne i nieprzyjemne miejsce'
meadowDesc='Łąka, słoneczna i zielona'
dessertDesc='Pustynia, piaszczysta i nudna jak flaki z olejem'
thickForrestDesc='Gęsty las, mroczne miejsce. W sam raz dla wiedźm.'
wildernessDesc='Las, gdzie dzikie zwierzęta czują się najlepiej'
villageDesc='Wioska, po środku karczma. Krowa robi "Muuuu...".'


hills = Field           (True,  False, True,  False, hillsDesc,        'hills',        [0,0])
riverValey = Field      (True,  False, True,  True,  riverValeyDesc,   'riverValey',   [1,0])
swamp = Field           (True,  False, False, True,  swampDesc,        'swamp',        [2,0])
marsch = Field          (True,  True,  False, True,  marschDesc,       'marsch',       [2,1])
meadow = Field          (True,  True,  True,  True,  meadowDesc,       'meadow',       [1,1])   # GAME STARTS HERE!
dessert = Field         (True,  True,  True,  False, dessertDesc,      'dessert',      [0,1])
thickForrest = Field    (False, True,  False, True,  thickForrestDesc, 'thickForrest', [2,2])
wilderness = Field      (True,  True,  True,  True,  wildernessDesc,   'wilderness',   [1,2])
village = Field         (True,  True,  True,  False, villageDesc,      'village',      [0,2])



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


