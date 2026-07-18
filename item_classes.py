
class Item:
    def __init__(self, name, description, rarity, value, type):
        self.name = name
        self.description = description
        self.rarity = rarity
        self.value = int(value)
        self.type = type
        
    def __str__(self):
        return f"Name: {self.name}\n Description: {self.description}\n Rarity: {self.rarity}\n Value: {self.value}\n Type: {self.type}"
        


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
        

name = input("Name: ")
descr = input("Description: ")
rar = input("Rarity: ")
val = input("Value: ")
dmg = input("Damage: ")
dur = input("Durability: ")

sword = Weapon(name, descr, rar, val, dmg, dur)
print("")
print(sword)
