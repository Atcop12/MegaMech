class Enemy(object):
    def __init__(self, Weapons, Armor, Movement, x, y, Number):
        self.Weapons = Weapons
        self.Armor = Armor
        self.Movement = Movement
        self.x = x
        self.y = y
        self.Number = Number

    def __repr__(self):
        return "{0} {1} {2}".format(self.Weapons, self.Armor, self.Movement)
