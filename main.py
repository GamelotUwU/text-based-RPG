import time
import random

class Battle:

    def __init__(self, hero, enemies):
        self.hero = hero
        self.enemies = enemies

    def start(self):

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
    

    




class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    def take_damage(self, dmg):
        self.health -= dmg

    def is_alive(self):
        return(self.health > 0)

class Hero(Character):

    exp_needed = 100
    base_dmg = 10
    max_health = 100

    def __init__(self, name, level, health, experience):
        super().__init__(name, health)
        self.level = level
        self.experience = int(experience)



    def level_up(self):
        self.level += 1
        self.health = self.max_health

    def __str__(self):
        return f"Character:{self.name} (Level {self.level}) \nHealth:{self.health}"
    
    def attack(self, enemy):
        enemy.take_damage(self.level * self.base_dmg)

    def gain_exp(self, enemy):
        self.experience += enemy.exp_points
        if self.experience >= self.exp_needed:
            self.level_up()
            self.experience = 0
        

   
class Enemy(Character):
    def __init__(self, name, health, damage, exp_points):
        super().__init__(name, health)
        self.damage = damage
        self.exp_points = int(exp_points)

    def __str__(self):
        return f"Enemy:{self.name} \nHealth:{self.health} \nAttack:{self.damage}\n"
    
    def attack(self, target):
        target.take_damage(self.damage)
    
    




enemy_list = []

print("Build character:")
name = input("Name:")
level = 1
health = int(input("Health:"))
hero = Hero(name,level,health, "0")

N = int(input("\nTypes of enemies:"))

for i in range(N):

    print("\nBuild enemy:")
    name = input("Name:")
    damage = int(input("Attack:"))
    health = int(input("Health:"))
    exp = input("XP points:")

    for j in range(2):
        enemy = Enemy(name,health,damage,exp)
        enemy_list.append(enemy)
        print("Enemy added")


time.sleep(5)

i = 0

battle = Battle(hero, enemy_list)
battle.start()








            


