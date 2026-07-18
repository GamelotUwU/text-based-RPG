#--- ITEM CLASS ---
class Item:
    def __init__(self, name:str, description:str, rarity:str, value:int, type:str):
        self.name = name
        self.description = description
        self.rarity = rarity
        self.value = value
        self.type = type
    
    def display_item_info(self):
        return (
            f"Name: {self.name}\n"
            f"Description: {self.description}\n"
            f"Rarity: {self.rarity}\n"
            f"Value: {self.value}\n"
            f"Type: {self.type}\n"
        )

#--- WEAPON CLASS ---
class Weapon(Item):
    def __init__(self, name:str, description:str, rarity:str, value:int, damage:int, durability:int):
        super().__init__(name, description, rarity, value, "Weapon")
        self.damage = damage
        self.durability = durability

    def display_item_info(self):
        return (
            super().display_item_info()
            + f"Damage: {self.damage}\n"
            + f"Durability: {self.durability}\n"
            )

#--- ARMOR CLASS ---
class Armor(Item):
    def __init__(self, name:str, description:str, rarity:str, value:int, defense:int, durability:int):
        super().__init__(name, description, rarity, value, "Armor")
        self.defense = defense
        self.durability = durability

    def display_item_info(self):
        return (
            super().display_item_info()
            + f"Defense: {self.defense}\n"
            + f"Durability: {self.durability}\n"
            )

#sword test
#sword = Weapon("Sword", "Just a Sword.", "EPIC", 1000, 60, 100)
#print(sword.display_item_info())

#helmet test
#helmet = Armor("Helmet", "Just a Helmet", "Common", 10, 25, 100)
#print(helmet.display_item_info())
