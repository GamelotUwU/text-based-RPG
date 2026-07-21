import time
import random


class Battle:

    def __init__(self, hero, enemies):
        self.hero = hero
        self.enemies = enemies


    def activate(self):

        enemy_index = 0
        random.shuffle(self.enemies)
    
        while True:

            time.sleep(5)

            if(enemy_index == len(self.enemies)):
                print(f"Hero {self.hero.name} has defeated all the enemies!\n")
                break

            enemy = self.enemies[enemy_index]       

            self.hero.attack(enemy)
            print(f"Hero {self.hero.name} attacks {enemy.name} for {self.hero.base_dmg * self.hero.level} damage!")
            print(f"{enemy.name} HP: {enemy.health}\n")
            if(not enemy.is_alive()):
                print(f"Hero {self.hero.name} has defeated {enemy.name}!\n")
                self.hero.gain_exp(enemy)
                enemy_index += 1
            else:
                enemy.attack(self.hero)
                print(f"{enemy.name} attacks hero {self.hero.name} for {enemy.damage}!")
                print(f"HP: {self.hero.health}\n")

            if(not self.hero.is_alive()):
                print(f"Hero {self.hero.name} died!\n")
                break
            pass
    