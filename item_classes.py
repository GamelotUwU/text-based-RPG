
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



class Chest:
    def __init__(self, loot = None):
        
        if loot == None:
            self.loot = []
        else:
            self.loot = loot
            
        self.is_open = False
    
    def open(self):
        if not self.is_open:
            self.is_open = True
            return self.loot

        return []
    
    def add_item(self, Item):
        if self.is_open == False:
            self.loot.append(Item)
    
    def __str__(self):
        return f"Chest(loot={[item.name for item in self.loot]})"


sword = Weapon("Sword of Rya", "This is a sword of a serpent", "Legendary", 1000, 77, 100)
helmet = Armor("Helmet of Fae", "Fae's magic helmet that grants you magic powers", "Legendary", 1000, 35, 100)

#custom items
bag = Item("bag", "a bag","Legendary",0,"bag1231924")

chest = Chest()

print(chest)

chest.add_item(sword)
chest.add_item(helmet)
chest.add_item(bag)

print(chest)

items = chest.open()

for item in items:
    print(item)

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
"""