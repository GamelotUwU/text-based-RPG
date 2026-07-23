from hero_class import Hero

class Shop():
    
    
    def __init__(self, item_list, hero, inventory):
        self.shop_list = []
        self.hero = hero
        self.item_list = item_list
        self.available_gold = int(hero.gold)
        self.inventory = inventory
        

    def buyable(self):
        for item, price in self.item_list:
            if self.available_gold > price:
                print(f"{item} can be bought by hero {hero.name}")
            else:
                print(f"{item} is currently too expensive for hero {hero.name}")
                
    def build_list(self):
        for item, price in self.item_list:
                item_string = f"{item}      {price} Gold"
                self.shop_list.append(item_string)
            
        
    
    def __str__(self):
            return "\n\n".join(self.shop_list)
        
    def sell(self, index):
        name, price = self.item_list[index]
        if(self.hero.gold >= price):
            self.inventory.append(self.item_list[index])
            self.hero.gold -= price
            self.item_list[index] = ("X", "")
            return True
        else:
            return False
            
        
        pass
            
        
    def open_shop(self):
        while True:
            
            
            self.build_list()
            
            print("\n\n".join(self.shop_list))
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
                print("Purchase successful!")
            else:
                print("Not enough Gold!")
        
    
    
        
inventory = []

hero = Hero("Test", 1, 150,0)
hero.gold = 35

lst = [("item1", 10), ("item2", 20), ("item3", 30), ("item4", 40)]
shop = Shop(lst, hero, inventory)
shop.open_shop()
print(inventory)
