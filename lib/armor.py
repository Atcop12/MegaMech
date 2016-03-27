class Armor(object):
    def __init__(self, HP, Name):
        self.Name = Name
        self.HP = HP

    def __repr__(self):
        return str(self.HP)
