class Weapon(object):
    def __init__(self, Range, Damage, Ammo, Name):
        self.Range = Range
        self.Damage = Damage
        self.Ammo = Ammo
        self.Name = Name

    def __repr__(self):
        return "{0} {1} {2}".format(self.Range, self.Damage, self.Ammo)
