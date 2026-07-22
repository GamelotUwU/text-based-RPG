from hero_class import Hero

class Shop():
    
    shop_list = []
    
    def __init__(self, item_list, hero):
        self.item_list = item_list
        self.available_gold = int(hero.gold)
        self.build_list()
        

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
            
        self.shop_list = "\n\n".join(self.shop_list)
        
    
    def __str__(self):
            return self.shop_list
        
    def sell(self, item,  inventory, hero, ):
        
        
        pass
            
        
    def open_shop(self,shop_list):
        while True:
            print(self.shop_list)
            option = input()
            if(option == "1"):
                self.sell(shop_list[0])
            elif(option == "2"):
                self.sell(shop_list[1])
            elif(option == "2"):
                self.sell(shop_list[2])
            elif(option == "2"):
                self.sell(shop_list[3])
            else:
                break
        
        pass
    
    
        
inventory = []

hero = Hero("Test", 1, 150,0)
hero.gold = 40

lst = [("item1", 10), ("item2", 20), ("item3", 30), ("item4", 40)]
shop = Shop(lst, hero)
print(shop)