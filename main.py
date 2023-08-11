import time
from game_functions import main
from game_functions import game_load
class Pokemon:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def display_info(self):
        print(f"""{self.name} is a {self.type}-type Pokémon with the ability {self.ability}.
              and has the following moves {self.move1}, {self.move2}, {self.move3}, {self.move4}  """)
    def gain_xp(self, amount):
        self.xp += amount
        print(f"{self.name} gained {amount} XP!")
        self.check_level_up()
    def display_xp(self):
        print(f"{self.name} has {self.xp} XP.")
    def check_level_up(self):
        if self.xp >= self.level * 100: # Example: 100 XP needed for each level
            self.level_up()
            self.xp = 0 # Reset XP after leveling up
class WaterPokemon(Pokemon):
    def __init__(self, name, type, ability, weakness, move1, move2, move3, move4, level, xp) -> None:
        super().__init__(name, type)
        self.ability = ability
        self.weakness = weakness
        self.move1 = move1
        self.move2 = move2
        self.move3 = move3
        self.move4 = move4
        self.level = level
        self.xp = 0

class FirePokemon(Pokemon): # Fixed class name
    def __init__(self, name, type, ability, weakness, move1, move2, move3, move4) -> None:
        super().__init__(name, 'fire')
        self.ability = ability
        self.weakness = weakness
        self.move1 = move1
        self.move2 = move2
        self.move3 = move3
        self.move4 = move4

class GrassPokemon(Pokemon): # Fixed class name
    def __init__(self, name, type, ability, weakness, move1, move2, move3, move4):
        super().__init__(name, 'grass') # Corrected to 'grass'
        self.ability = ability
        self.weakness = weakness
        self.move1 = move1
        self.move2 = move2
        self.move3 = move3
        self.move4 = move4 # Added missing attributes

# Creating instances of the child classes
squirtle = WaterPokemon("Squirtle", "water", "torrent", "grass", 'tackle', 'tail whip', 'watergun', 'mist',1, 0)
charmander = FirePokemon('Charmander', 'fire', 'Blaze', 'water', 'scratch', 'tackle', 'ember', 'growl') # Fixed class name
bulbasaur = GrassPokemon('Bulbasaur', 'grass', 'overgrow', 'fire', 'scratch', 'tackle', 'ember', 'growl') # Fixed class name and removed extra parentheses

# main function
game_load()
time.sleep(2)
main()

# Using the display_info method inherited from the parent class
squirtle.display_info()  # Output: "Squirtle is a water-type Pokémon with the ability torrent."
charmander.display_info()  # Output: "Charmander is a fire-type Pokémon with the ability Blaze."
bulbasaur.display_info()  # Output: "Bulbasaur is a grass-type Pokémon with the axbility overgrow."
squirtle.gain_xp(100)
print(f"{squirtle.name} has {squirtle.xp} XP.") # Output: "Charmander has 100 XP."
