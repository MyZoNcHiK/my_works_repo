from abc import ABC, abstractmethod

class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

class Potion:
    def __init__(self, heal_amount):
        self.heal_amount = heal_amount

class Character:
    def __init__(self, name, hp, weapon):
        self.name = name
        self.hp = hp
        self.weapon = weapon

    def attack(self):
        print(f"{self.name} атакує зброєю {self.weapon.name}")
        print(f"Завдано шкоди: {self.weapon.damage}")

    def drink_potion(self, potion):
        self.hp += potion.heal_amount
        print(f"{self.name} використав зілля")
        print(f"Здоров'я відновлено на {potion.heal_amount}")
        print(f"Поточне здоров'я: {self.hp}")

class CombatActions(ABC):
    @abstractmethod
    def attack(self, target):
        pass
    @abstractmethod
    def defend(self):
        pass

class Warrior(CombatActions):
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, target):
        target.hp -= self.damage
        print(f"{self.name} атакує {target.name}")
        print(f"Завдано шкоди: {self.damage}")
        print(f"Здоров'я противника: {target.hp}")

    def defend(self):
        print(f"{self.name} переходить у захист")


sword = Weapon("меч", 25)
potion = Potion(30)

hero = Character("герой", 100, sword)
enemy = Character("орк", 80, sword)
warrior = Warrior("воїн", 120, 35)

hero.attack()
hero.drink_potion(potion)

warrior.attack(enemy)
warrior.defend()
