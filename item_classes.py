import random


class Item:
    def __init__(self, name, description, rarity, value, type):
        self.name = name
        self.description = description
        self.rarity = rarity
        self.value = int(value)
        self.type = type
        
    def __str__(self):
        return f"""
Name: {self.name}
Description: {self.description}
Rarity: {self.rarity}
Value: {self.value}
Type: {self.type}
"""
 


class Weapon(Item):
    def __init__(self, name, description, rarity, value, damage, durability):
        super().__init__(name, description, rarity, value, "Weapon")
        self.damage = int(damage)
        self.durability = int(durability)
        
    def __str__(self):
            return f"""
Name: {self.name}
Description: {self.description}
Rarity: {self.rarity}
Value: {self.value}
Damage: {self.damage}
Durability: {self.durability}
"""



class Armor(Item):
    def __init__(self, name, description, rarity, value, defense, durability):
        super().__init__(name, description, rarity, value, "Armor")
        self.defense = int(defense)
        self.durability = int(durability)

    
    def __str__(self):
        return f"""
Name: {self.name}
Description: {self.description}
Rarity: {self.rarity}
Value: {self.value}
Type: {self.type}
Defense: {self.defense}
Durability: {self.durability}
"""

class Gold_Bag():
    def __init__(self):
        self.gold = random.randint(10, 100)

    def __str__(self):
        return f"Gold bag containing {self.gold} Gold"
    
    def amount(self):
        return self.gold
    


""" list = []

for i in range(5):
    bag = Gold_Bag()
    list.append(bag)

for bag in list:
    print(bag) """