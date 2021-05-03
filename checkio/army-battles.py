#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

# Taken from mission The Warriors

class Warrior:
    health = 50
    attack = 5
    
    @property
    def is_alive(self):
        return self.health > 0

class Knight(Warrior):
    attack = 7

def fight(unit_1, unit_2):
    while unit_1.is_alive and unit_2.is_alive:
        unit_2.health -= unit_1.attack
        if unit_2.is_alive: unit_1.health -= unit_2.attack
    return unit_1.is_alive
    
class Army:
    
    def __init__(self):
        self.units = []
    
    def add_units(self, cls, count):
        self.units += [cls() for _ in range(count)]
        
    @property
    def is_alive(self):
        return any([unit.is_alive for unit in self.units])
        
    @property
    def current_unit(self):
        return [unit for unit in self.units if unit.is_alive][0]
    
class Battle:
    def fight(self, army_1, army_2):
        while army_1.is_alive and army_2.is_alive:
            fight(army_1.current_unit, army_2.current_unit)
            
        return army_1.is_alive

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    
    #fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    #battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)
    
    army_4 = Army()
    army_4.add_units(Warrior, 30)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")
