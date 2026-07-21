from hero_class import Hero

class Shop():
    def __init__(self, item_list, hero):
        self.item_list = item_list
        self.available_gold = int(hero.gold)

    def buyable(self):
        for item, price in self.item_list:
            if self.available_gold > price:
                print(f"{item} can be bought by hero {hero.name}")
            else:
                print(f"{item} is currently too expensive for hero {hero.name}")

hero = Hero("Test", 1, 150,0)
hero.gold = 15

lst = [("item1", 10), ("item2", 20), ("item3", 30)]
shop = Shop(lst, hero)
shop.buyable()