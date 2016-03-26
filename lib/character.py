class Character(object):
    def __init__(self, Weapons, Armor, Movement, x, y, Money, CampaignLevel, Level, XP):
        self.Weapons = Weapons
        self.Armor = Armor
        self.Movement = Movement
        self.x = x
        self.y = y
        self.Money = Money
        self.CampaignLevel = CampaignLevel
        self.XP = XP
        self.Level = Level

    def __repr__(self):
        return "{0} {1} {2}".format(self.Weapons, self.Armor, self.Movement)

    def subtract_money(self, amount):
        """Subtract money. Returns True if valid amount
        subtracted. Returns False if character does not
        have enough money"""
        if self.Money - amount >= 0:
            self.Money = self.Money - amount
            return True
        return False

    def add_money(self, amount):
        """Add money"""
        self.Money = self.Money + amount
