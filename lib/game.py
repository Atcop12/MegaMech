import math
import random

from lib import Armor
from lib import Weapon
from lib import Character
from lib import Enemy

board = []
MyCharacter = Character([], [], 0, 0, 0, 1000, 1, 0, 0)

class Game(object):
    def __init__(self):
        print "Welcome to the MegaMech game"

    def Shop(self):
        print("You have $" + str(MyCharacter.Money))
        print("Your Level is " + str(MyCharacter.Level))
        print("~~~~~~~~~~~~~~~~~~Shop~~~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~~~~~~Armor~~~~~~~~~~~~~~~~~")
        print("Name---------------HP--------------Price")
        print("Tin		  50		    200")
        print("Bronze		  100		    500")
        print("~~~~~~~~~~~~~~~~~Weapons~~~~~~~~~~~~~~~~")
        print("Name----Damage----Ammo----Range----Price")
        print("Sword   5         inf     0        200")
        print("Gun     5         10      3        500")
        print("~~~~~~~~~~~Personal~Upgrades~~~~~~~~~~~~")
        print("Name------------------------------Effect")
        print("Walk speed			   +1")
        choice = raw_input("Which one do you want?(Type the name, or say 'Cancel'.) ")
        if choice == "Tin" and MyCharacter.Money >= 200 and len(MyCharacter.Armor) + 1 <= float(MyCharacter.Level+1)/3 + 1:
            MyCharacter.Money -= 200
            MyCharacter.Armor.append(Armor(50, "Tin"))
        elif choice == "Bronze" and MyCharacter.Money >= 500 and len(MyCharacter.Armor) + 1 <= float(MyCharacter.Level+1)/3 + 1:
            MyCharacter.Money -= 500
            MyCharacter.Armor.append(Armor(100, "Bronze"))
        elif choice == "Sword" and MyCharacter.Money >= 200 and len(MyCharacter.Weapons) + 1 <= float(MyCharacter.Level+1)/3 + 1:
            MyCharacter.Money -= 200
            MyCharacter.Weapons.append(Weapon(0, 5, float('inf'), "Sword"))
        elif choice == "Gun" and MyCharacter.Money >= 500 and len(MyCharacter.Weapons) + 1 <= float(MyCharacter.Level+1)/3 + 1:
            MyCharacter.Money -= 500
            MyCharacter.Weapons.append(Weapon(3, 5, 10, "Gun"))
        elif choice == "Walk speed" and MyCharacter.Money >= 200:
            MyCharacter.Money -= 200
            MyCharacter.Movement = MyCharacter.Movement + 1
        elif choice == "Cancel":
            Selling = raw_input("Sell or next level? ")
            if Selling == "Sell":
                self.Sell()
            return
        elif choice != "Cancel":
            print("Sorry I didn't catch that.")
            self.Shop()
            return
            
    def Mores(self):
        More = raw_input("Would you like to buy more?(Yes/No) ")
        if More == "Yes":
            self.Shop()
        elif More == "No":
            Selling = raw_input("Sell or next level? ")
            if Selling == "Sell":
                self.Sell()
                return
            elif Selling != "next level":
                print("Sorry I dodn't catch that.")
                self.Mores()
        else:
            print("Sorry I didn't catch that. ")
            self.Mores()
        

    def Sell(self):
        for Armor in MyCharacter.Armor:
            print(Armor.Name)
        for Weapon in MyCharacter.Weapons:
            print(Weapon.Name)
        print("Walk speed (" + str(MyCharacter.Movement) + ")")
        Choice = raw_input("Which one do you want to sell?(Name of item) ")
        NewList = []
        AOW = len(MyCharacter.Weapons)
        AOA = len(MyCharacter.Armor)
        WS = MyCharacter.Movement
        Number = 1
        for Armor in range(len(MyCharacter.Armor)):
            if Choice == MyCharacter.Armor[Armor].Name and Number == 1:
                Number = 2
                if Choice == "Tin":
                    MyCharacter.Money += 200
                    print("Tin")
                elif MyCharacter.Armor[Armor].Name == "Bronze":
                    MyCharacter.Money += 500
                    print("Bronze")
                else:
                    print("Glitch")
            else:
                NewList.append(MyCharacter.Armor[Armor])
        MyCharacter.Armor = NewList
        NewList = []
        for Weapon in range(len(MyCharacter.Weapons)):
            if Choice == MyCharacter.Weapons[Weapon].Name and Number == 1:
                Number = 2
                if Choice == "Sword":
                    MyCharacter.Money += 200
                elif Choice == "Gun":
                    MyCharacter.Money += 500
            else:
                NewList.append(MyCharacter.Weapons[Weapon])
        MyCharacter.Weapons = NewList
        if Choice == "Walk speed" and MyCharacter.Movement > 0:
            MyCharacter.Movement -= 1
            MyCharacter.Money += 200
        if AOW != len(MyCharacter.Weapons) or AOA != len(MyCharacter.Armor) or WS != MyCharacter.Movement:
            Answere = raw_input("Do you want to sell more?(Yes/No)")
            if Answere == "Yes":
                self.Sell()
            else:
                Answere2 = raw_input("Shop or next level? ")
                if Answere2 == "Shop":
                    self.Shop()
                    return
        elif not Sold:
            print("I didn't quite catch that")
            self.Sell()
        def Shopping():
            choice = raw_input("Shop, Sell, or next level? ")
            if choice == "Shop":
                self.Shop()
            elif choice == "Sell":
                self.Sell()
            elif choice != "next level":
                print("Sorry I didn't catch that.")
                Shopping()
        Shopping()
        return

    def IsInt(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    def Move_Enemy(self, Enemy):
        board[int(Enemy.y)][int(Enemy.x)] = "-"
        distancex = int(MyCharacter.x) - int(Enemy.x)
        if distancex < 0:
            distancex = distancex * -1
        distancey = int(MyCharacter.y) - int(Enemy.y)
        if distancey < 0:
            distancey = distancey * -1
        distance = distancex
        if distance < distancey:
            distance = distancey
        if distance <= Enemy.Movement:
            Enemy.y = MyCharacter.y
            Enemy.x = MyCharacter.x
        else:
            if int(MyCharacter.x) > int(Enemy.x):
                Enemy.x = Enemy.x + Enemy.Movement
            if int(MyCharacter.y) > int(Enemy.y):
                Enemy.y = Enemy.y + Enemy.Movement
            if int(MyCharacter.x) < int(Enemy.x):
                Enemy.x = Enemy.x - Enemy.Movement
            if int(MyCharacter.y) < int(Enemy.y):
                Enemy.y = Enemy.y - Enemy.Movement

    def print_board(self, board):
        for row in board:
            print(" ".join(row))
    for x in range(10):
        board.append(["-"] * 10)

    def Level(self, Enemies, Money, XP1):
        for x in board:
            for y in x:
                y = "-"
        MyCharacter.x = 0
        MyCharacter.y = 0
        print("Your Level is " + str(MyCharacter.Level))
        for Enemy in Enemies:
            board[Enemy.y][Enemy.x] = str(Enemies[Enemy.Number].Number)
        board[int(MyCharacter.y)][int(MyCharacter.x)] = "X"
        self.print_board(board)
        print("")
        EnemiesDestroyed = 0
        def attack(EnemiesDestroyed):
            NumberOfEnemies = len(Enemies)
            answere = raw_input("Would you like to attack?(Yes/No) ")
            if answere == "Yes":
                print("Choose your weapon. ")
                for Weapon in MyCharacter.Weapons:
                    print(Weapon.Name)
                Weapon = raw_input("(Weapon name) ")
                print("Choose an enemy.")
                for Enemy in Enemies:
                    if Enemy.Armor[len(Enemy.Armor) - 1]:
                        print(Enemy.Number)
                Enemy = raw_input("(Name of enemy)" )
                if IsInt(Enemy) and int(Enemy) <= len(Enemies)-1:
                    Enemy = Enemies[int(Enemy)]
                else:
                    print("Sorry I didn't catcth that")
                    attack(EnemiesDestroyed)
                    return EnemiesDestroyed
                distancex = int(MyCharacter.x) - int(Enemy.x)
                if distancex < 0:
                    distancex = distancex * -1
                distancey = int(MyCharacter.y) - int(Enemy.y)
                if distancey < 0:
                    distancey = distancey * -1
                distance = distancex
                if distance < distancey:
                    distance = distancey
                Number = 1
                for Thing in MyCharacter.Weapons:
                    if Thing.Name == Weapon:
                        if Thing.Range >= distance and Thing.Ammo >= 1:
                            for Armor in Enemy.Armor:
                                if Armor.HP > 0:
                                    ArmorUsing = Armor
                                    break
                            else:
                                print("That enemy is already dead.")
                                attack(EnemiesDestroyed)
                                return EnemiesDestroyed
                            Damage = float(Thing.Damage) * float(random.randint(9, 11))/float(10) * (float(MyCharacter.Level)/float(10) + float(1))
                            ArmorUsing.HP = float(ArmorUsing.HP) - float(Damage)
                            print("You did " + str(Damage) + " damage.")
                            Thing.Ammo -= 1
                            if ArmorUsing.HP <= 0:
                                for Armor in Enemy.Armor:
                                    if Armor.HP > 0:
                                        Armor.HP = Armor.HP + ArmorUsing.HP
                                        ArmorUsing.HP = 0
                                        break
                                else:
                                    EnemiesDestroyed += 1
                                    print("EnemiesDestroyed: " + str(EnemiesDestroyed))
                                    if EnemiesDestroyed == NumberOfEnemies:
                                        return "Game Over"
                    elif Number == len(MyCharacter.Weapons):
                        print("Sorry I didn't catch that.")
                        attack(EnemiesDestroyed)
                    Number += 1
            elif answere != "No":
                print("Sorry I didn't catch that")
                attack(EnemiesDestroyed)
            return EnemiesDestroyed

    def Inputs(self):
        board[int(MyCharacter.y)][int(MyCharacter.x)] = "-"
        x = raw_input("X: ")
        y = raw_input("Y: ")
        if IsInt(x) and IsInt(y):
            distancex = int(MyCharacter.x) - (int(x) - 1)
        else:
            print("Sorry I didn't quite catch that.")
            self.Inputs()
            return
        if distancex < 0:
            distancex = (distancex * -1)
        distancey = int(MyCharacter.y) - (int(y) - 1)
        if distancey < 0:
            distancey = distancey * -1
        distance = distancex
        if distance < distancey:
            distance = distancey
        if distance <= MyCharacter.Movement:
            MyCharacter.x = str(int(x) - 1)
            MyCharacter.y = str(int(y) - 1)
        else:
            print("Sorry that's to far away.")
            self.Inputs()

        def AIAttack(self, Enemy):
            PosWeps = []
            WeaponToBeUsed = ""
            distancex = int(MyCharacter.x) - int(Enemy.x)
            if distancex < 0:
                distancex = distancex * -1
            distancey = int(MyCharacter.y) - int(Enemy.y)
            if distancey < 0:
                distancey = distancey * -1
            distance = distancex
            if distance < distancey:
                distance = distancey
            for Weapon in Enemy.Weapons:
                if Weapon.Range >= distance and Weapon.Ammo >= 1:
                    PosWeps.append(Weapon)
            HighestDamage = 0
            for Weapon in PosWeps:
                if Weapon.Damage > HighestDamage:
                    WeaponToBeUsed = Weapon
                    HighestDamage = Weapon.Damage
            if WeaponToBeUsed != "":
                for Armor in MyCharacter.Armor:
                    if Armor.HP > 0:
                        WeaponToBeUsed.Ammo -= 1
                        ArmorUsing = Armor
                        ArmorUsing.HP = ArmorUsing.HP - WeaponToBeUsed.Damage * float(random.randint(9, 11))/10/(float(MyCharacter.Level)/10 + 1)
                        TotalHP = 0
                        for Armor in MyCharacter.Armor:
                            TotalHP += Armor.HP
                        print("My health: " + str(TotalHP))
                        break
        while True:
            for x in range(10):
                for y in range(10):
                    board[y][x] = "-"
            if MyCharacter.Armor[len(MyCharacter.Armor) - 1].HP <= 0:
                print("You Loose.")
                MyCharacter.Money = 1000
                MyCharacter.CampaignLevel = 1
                MyCharacter.Armor = []
                MyCharacter.Weapons = []
                MyCharacter.Movement = 0
                self.Shop()
                return
            self.Inputs()
            attacking = attack(int(EnemiesDestroyed))
            if attacking == "Game Over":
                print("You win!")
                MyCharacter.XP += XP1
                if MyCharacter.XP >= 100 * (MyCharacter.Level + 1):
                    MyCharacter.XP -= 100 * (MyCharacter.Level + 1)
                    MyCharacter.Level += 1
                    print("You Leveled up to level: " + str(MyCharacter.Level) + "!")
                MyCharacter.Money += Money
                MyCharacter.CampaignLevel += 1
                print("You now have $" + str(MyCharacter.Money))
                break
            else:
                EnemiesDestroyed = attacking
            for Enemy in Enemies:
                for Armor in Enemy.Armor:
                    if Armor.HP > 0:
                        ArmorUsing = Armor
                        Move_Enemy(Enemy)
                        AI = AIAttack(Enemy)
                        board[int(Enemy.y)][int(Enemy.x)] = str(Enemies[int(Enemy.Number)].Number)
                        break
            if MyCharacter.Armor[len(MyCharacter.Armor) - 1].HP <= 0:
                print("You Loose.")
                MyCharacter.Money = 1000
                MyCharacter.CampaignLevel = 1
                MyCharacter.Armor = []
                MyCharacter.Weapons = []
                MyCharacter.Movement = 0
                self.Shop()
                return
            board[int(MyCharacter.y)][int(MyCharacter.x)] = "X"
            self.print_board(board)
            print("")
        MyCharacter.x = 0
        MyCharacter.y = 0
        for Armor in MyCharacter.Armor:
            if Armor.Name == "Tin":
                Armor.HP = 50
            elif Armor.Name == "Bronze":
                Armor.HP = 100

    def Shopping(self):
        choice = raw_input("Shop, Sell, or next level? ")
        if choice == "Shop":
            self.Shop()
        elif choice == "Sell":
            self.Sell()
        elif choice != "next level":
            print("Sorry I didn't catch that.")
            self.Shopping()

    def start(self):
        self.Shop()

        while True:
            if MyCharacter.CampaignLevel == 1:
                self.Level([Enemy([Weapon(0, 5, float('inf'), "Sword")], [Armor(50, "Tin")], 1, 9, 9, 0)], 100, 100)
            elif MyCharacter.CampaignLevel == 2:
                self.Level([Enemy([Weapon(0, 5, float('inf'), "Sword")], [Armor(50, "Tin")], 1, 9, 0, 0), Enemy([Weapon(0, 5, float('inf'), "Sword")], [Armor(50, "Tin")], 1, 0, 9, 1)], 300, 300)
            elif MyCharacter.CampaignLevel == 3:
                self.Level([Enemy([Weapon(0, 5, float('inf'), "Sword")], [Armor(50, "Tin")], 1, 9, 0, 0), Enemy([Weapon(0, 5, float('inf'), "Sword")], [Armor(50, "Tin")], 1, 0, 9, 1), Enemy([Weapon(0, 5, float('inf'), "Sword"), Weapon(3, 5, 10, "Gun")], [Armor(100, "Bronze")], 2, 9, 9, 2)], 500, 500)
            elif MyCharacter.CampaignLevel == 4:
                self.Level([Enemy([Weapon(0, 5, float('inf'), "Sword"), Weapon(3, 5, 10, "Gun")], [Armor(100, "Bronze"), Armor(100, "Bronze")], 2, 9, 9, 0)], 700, 700)
            else:
                print("YOU JUST WON THE GAME!!!!")
                break
