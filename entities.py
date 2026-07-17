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
    