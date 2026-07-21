from item_classes import Item, Weapon, Armor
from loot_pool import WEAPONS, ARMORS
import random

RARITIES = [
    "Common",
    "Rare",
    "Epic",
    "Legendary"
]

RARITY_MULTIPLIER = {
    "Common": 1.0,
    "Rare": 1.3,
    "Epic": 1.7,
    "Legendary": 2.2
}

class loot_generator:
    def generate_weapon():
        weapon_choice = random.choice(WEAPONS)
        name = weapon_choice["name"]
        description = weapon_choice["description"]
        rarity = random.choice(RARITIES)
        damage = int(weapon_choice["base_damage"] * RARITY_MULTIPLIER[rarity]) #base damage multipled by rarity
        value = int(weapon_choice["base_value"] * RARITY_MULTIPLIER[rarity])
        durability = 100

        return Weapon(name, description, rarity, value, damage, durability)
    
    def generate_armor():
        armor_choice = random.choice(ARMORS)
        name = armor_choice["name"]
        description = armor_choice["description"]
        rarity = random.choice(RARITIES)
        defense = int(armor_choice["base_defense"] * RARITY_MULTIPLIER[rarity])
        value = int(armor_choice["base_value"] * RARITY_MULTIPLIER[rarity])
        durability = 100

        return Armor(name, description, rarity, value, defense, durability)
    
    #def generate_items()