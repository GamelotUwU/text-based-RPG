from character_class import Character


class Monster(Character):
    def __init__(self, name, health, damage, exp_points):
        super().__init__(name, health)
        self.damage = damage
        self.exp_points = int(exp_points)

    def __str__(self):
        return f"Enemy:{self.name} \nHealth:{self.health} \nAttack:{self.damage}\n"
    
    def attack(self, target):
        target.take_damage(self.damage)
    