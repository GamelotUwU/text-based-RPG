from character_class import Character

class Hero(Character):

    exp_needed = 100
    base_dmg = 10
    max_health = 100
    gold = 0

    def __init__(self, name, level, health, experience):
        super().__init__(name, health)
        self.level = level
        self.experience = int(experience)

    def gain_gold(self, item):
        self.gold += item.amount()

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
        