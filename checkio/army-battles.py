#!/usr/bin/python3
# -*-coding:utf-8-*-

__author__ = "Bannings"

# Taken from mission The Warriors
class Warrior:
    health = 50
    attack = 5
    defense = 0
    
    @property
    def is_alive(self):
        return self.health > 0
    
    def fight(self, units):
        another = units[0]
        another.health -= max(self.attack - another.defense, 0)

    def __repr__(self):
        return f'{type(self).__name__} {self.health} {self.attack} {self.defense}'

class Defender(Warrior):
    health = 60
    attack = 3
    defense = 2
    
class Rookie(Warrior):
    health = 50
    attack = 1
    
class Knight(Warrior):
    attack = 7

class Vampire(Warrior):
    health = 40
    attack = 4
    vampirism = 50
    
    def fight(self, units):
        original_health = units[0].health
        super().fight(units)
        harm = original_health - units[0].health
        self.health += harm * self.vampirism / 100

class Lancer(Warrior):
    health = 50
    attack = 6

    def fight(self, units):
        super().fight(units)
        if len(units) > 1:
            units[1].health -= max(self.attack // 2 - units[1].defense, 0)

class Healer(Warrior):
    health = 60
    attack = 0
    
    def heal(self, unit: Warrior):
        unit.health = min(unit.health + 2, unit.__class__.health)

def fight(unit_1, unit_2):
    while unit_1.is_alive and unit_2.is_alive:
        unit_1.fight([unit_2])
        if unit_2.is_alive: unit_2.fight([unit_1])
    return unit_1.is_alive
    
class Army:
    
    def __init__(self):
        self.units = []
    
    def add_units(self, cls, count):
        self.units += [cls() for _ in range(count)]
    
    def fight(self, another):
        self.units[0].fight(another.units)
        # while self.units and self.units[0].health <= 0: self.units.pop(0)
        while another.units and another.units[0].health <= 0: another.units.pop(0)

        if len(self.units) > 1 and isinstance(self.units[1], Healer):
            self.units[1].heal(self.units[0])
        
    @property
    def is_alive(self):
        return bool(self.units)
    
class Battle:
    def fight(self, army_1, army_2):
        while army_1.is_alive and army_2.is_alive:
            unit_1, unit_2 = army_1.units[0], army_2.units[0]
            army_1.fight(army_2)

            if unit_1.is_alive and unit_2.is_alive:
                army_2.fight(army_1)
            
        return army_1.is_alive

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    
    #fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()
    eric = Vampire()
    adam = Vampire()
    richard = Defender()
    ogre = Warrior()
    freelancer = Lancer()
    vampire = Vampire()
    priest = Healer()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True
    assert fight(eric, richard) == False
    assert fight(ogre, adam) == True
    assert fight(freelancer, vampire) == True
    assert freelancer.is_alive == True
    assert freelancer.health == 14    
    priest.heal(freelancer)
    assert freelancer.health == 16

    #battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Healer, 1)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Lancer, 2)
    my_army.add_units(Healer, 1)
    my_army.add_units(Warrior, 1)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Lancer, 4)
    enemy_army.add_units(Healer, 1)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)
    enemy_army.add_units(Healer, 1)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Lancer, 1)
    army_3.add_units(Healer, 1)
    army_3.add_units(Defender, 2)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 1)
    army_4.add_units(Healer, 1)
    army_4.add_units(Lancer, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")
