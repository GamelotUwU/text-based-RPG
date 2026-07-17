import time

from entities import Hero, Enemy
from node_classes import Battle


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

battle = Battle(hero, enemy_list)
battle.start()








            


