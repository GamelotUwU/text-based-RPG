class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    def take_damage(self, dmg):
        self.health -= dmg

    def is_alive(self):
        return(self.health > 0)
    




   
   
