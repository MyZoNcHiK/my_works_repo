from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def defend(self):
        pass

    @abstractmethod
    def use_skill(self):
        pass

class Warrior(Character):
    def attack(self):
        print(f"{self.name} атакує мечем")

    def defend(self):
        print(f"{self.name} блокує атаку щитом")

#    def use_skill(self):
#        print(f"{self.name} використовує вміння лють")

class Mage(Character):
    def attack(self):
        print(f"{self.name} атакує магічною кулею")

    def defend(self):
        print(f"{self.name} створює магічний бар'єр")

    def use_skill(self):
        print(f"{self.name} використовує вогняну кулю")

try:
    character = Character("Герой", 100)
except TypeError as error:
    print(error)

try:
    warrior = Warrior("Артур", 150)
except TypeError as error:
    print(error)


mage = Mage("Мерлін", 100)
print(f"Маг: {mage.name}, здоров'я: {mage.hp}")
mage.attack()
mage.defend()
mage.use_skill()
