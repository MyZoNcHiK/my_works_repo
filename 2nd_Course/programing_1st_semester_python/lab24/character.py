class Character:pass
class Warrior(Character):pass
class Mage(Character):pass
class BattleMage(Warrior, Mage):pass
class EliteBattleMage(BattleMage):pass


print("EliteBattleMage:", EliteBattleMage.__mro__)
print(Mage.__mro__)



