from item_classes import Item, Weapon, Armor

class Chest:
    # def __init__(self, loot = None):
        

    def add_item(self, Item):
        if not self.is_open:
            self.loot.append(Item)
    
    def __str__(self):
        list = "\n- ".join([item.name for item in self.loot])
        return f"Chest loot: \n- {list}"
    


sword = Weapon("Sword of Rya", "This is a sword of a serpent", "Legendary", 1000, 77, 100)
helmet = Armor("Helmet of Fae", "Fae's magic helmet that grants you magic powers", "Legendary", 1000, 35, 100)

#custom items
bag = Item("bag", "a bag","Legendary",0,"bag1231924")

chest = Chest()


chest.add_item(sword)
chest.add_item(helmet)
chest.add_item(bag)

print(chest)

items = chest.open()

for item in items:
    print(item)

