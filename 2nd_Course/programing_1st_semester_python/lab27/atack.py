from abc import ABC, abstractmethod

def double_damage(func):
    def wrapper(self):
        return func(self) * 2
    return wrapper


def damage_bonus(func):
    def wrapper(self):
        return func(self) + 20
    return wrapper


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

class Mage(Character):
    @double_damage
    @damage_bonus
    def attack(self):
        print(f"{self.name} атакує магічною кулею")
        return 30

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

print("Сила атаки:", mage.attack())
