from hero_class import Hero
from loot_generator import loot_generator
import random

class Shop():
    
    
    def __init__(self, hero):
        self.shop_list = []
        self.item_list = []
        self.hero = hero
        self.available_gold = int(hero.gold)
        self.create_list()
        
        

    """ def buyable(self):
        for item, price in self.item_list:
            if self.available_gold > price:
                print(f"{item} can be bought by hero {hero.name}")
            else:
                print(f"{item} is currently too expensive for hero {hero.name}") """
                
    def build_list(self):

        self.shop_list.clear()

        for item in self.item_list:
                item_string = self.arrange_on_shelf(item)
                self.shop_list.append(item_string)
            
        
    
    def __str__(self):
            return "\n\n".join(self.shop_list)
        
    def sell(self, index):
        name, price = self.item_list[index]
        if(self.hero.gold >= price):
            self.hero.hero_inventory.append(self.item_list[index])
            self.hero.gold -= price
            self.item_list[index] = ("X", "")
            return True
        else:
            return False
            

        
    def open_shop(self):
        while True:
            
            
            self.build_list()
            
            print("         ".join(self.shop_list[:2]))
            print("         ".join(self.shop_list[2:]))
            print("\n")
            option = input()
            if(option == "1"):
                result = self.sell(0)
            elif(option == "2"):
                result = self.sell(1)
            elif(option == "3"):
                result = self.sell(2)
            elif(option == "4"):
                result = self.sell(3)
            else:
                break
            
            if(result):
                print("Purchase successful!\n")
            else:
                print("Not enough Gold!\n")

    def create_list(self):
        for i in range(4):
            self.store_item = loot_generator.generate_weapon()
            weapon_list.append(self.store_item)
            item = f"{self.store_item.name}({self.store_item.rarity})"
            price = self.store_item.value
            self.store_item = (item, price)
            self.item_list.append(self.store_item)

    def arrange_on_shelf(self, item):
        shelf_length = 20
        shelf_name, shelf_price = item
        empty_space = shelf_length - (len(shelf_name) + len(str(shelf_price)))
        shelf_item = shelf_name
        for i in range(empty_space):
            shelf_item += " "
        shelf_item += str(shelf_price)
        return shelf_item  

     
        



    

hero = Hero("Test", 1, 150,0)
hero.gold = 100
shop_list = []
weapon_list = []


shop = Shop(hero)
shop.open_shop()
print(f"Hero currently has:{hero.hero_inventory}")

