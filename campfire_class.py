from hero_class import Hero

class Campfire:

    def __init__(self, hero):
        self.hero = hero

    def light_campfire(self):
        while True:
            print("\nYou have found a campfire hero, you can relax here for a while\n")
            print("1.Rest(Heal for 30% Max HP)")
            print("2.Strenghten yourself(Upgrade base damage by 20%)\n")
            option = input()

            if(option == "1"):
                self.heal()
            elif(option == "2"):
                self.strenghten()
            else:
                break

    def heal(self):
        temp_health = self.hero.health + int((30 * self.hero.max_health) / 100)
        if(temp_health <= self.hero.max_health):
            self.hero.health = temp_health
        else:
            self.hero.health = self.hero.max_health
        print(f"Hero Hp: {self.hero.health}")

    def strenghten(self):
        self.hero.base_dmg += int((20 * self.hero.base_dmg) / 100)
        print(f"Hero Dmg: {self.hero.base_dmg}")


