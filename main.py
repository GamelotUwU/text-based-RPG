import time


class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    def take_damage(self, dmg):
        self.health -= dmg


class Hero(Character):

    exp_needed = 100
    base_dmg = 10

    def __init__(self, name, level, health, experience):
        super().__init__(name, health)
        self.level = level
        self.experience = int(experience)


    def level_up(self):
        self.level += 1

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
    
    def take_damage(self, dmg):
        self.health -= dmg
    




enemy_list = []

print("Build character:")
name = input("Name:")
level = 1
health = int(input("Health:"))
hero = Hero(name,level,health, "0")

print("\nBuild enemy:")
name = input("Name:")
damage = int(input("Attack:"))
health = int(input("Health:"))

for i in range(5):
    enemy = Enemy(name,health,damage,"50")
    enemy_list.append(enemy)

i = 0

time.sleep(5)


while True:

    enemy = enemy_list[i]
    dmg = enemy.damage
    hero.attack(enemy)
    print(f"\nHero {hero.name} attacks {enemy.name} for {hero.level * hero.base_dmg} damage!")
    print(f"{enemy.name} HP: {enemy.health}")
    if(enemy.health <= 0):
        print(f"Hero {hero.name} has defeated {enemy.name}!")
        hero.gain_exp(enemy)
        i += 1
        if(i == len(enemy_list)):
            print(f"Hero {hero.name} has defeated all enemies!")
            break
    hero.take_damage(dmg)
    print(f"Hero {hero.name} has taken {dmg} damage from {enemy.name}!")
    print(f"HP: {hero.health}\n")
    time.sleep(5)

    if(hero.health == 0):
        print("You died!")
        break



            


