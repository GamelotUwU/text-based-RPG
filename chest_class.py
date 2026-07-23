from item_classes import Item, Weapon, Armor
from loot_generator import loot_generator
import random

class Chest():
    def __init__(self):
        super().__init__()
        self.is_open = False
        self.loot = []
    
    def activate(self):
        number_of_items = random.randint(0, 5)

        for _ in range(number_of_items):
            if random.random() < 0.5:
                self.loot.append(loot_generator.generate_weapon())
            else:
                self.loot.append(loot_generator.generate_armor())

        return self.loot
    

    def __str__(self):
        if not self.loot:
            return "Empty chest"
        
        list = "\n- ".join([item.name for item in self.loot])
        return f"Chest loot: \n- {list}"



chest = Chest()

items = chest.open()

for item in items:
    print(item)

print(chest)