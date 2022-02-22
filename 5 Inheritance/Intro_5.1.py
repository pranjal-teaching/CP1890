class Monster:
    def __init__(self, hitpoints, damage, range):
        self.hitpoints = hitpoints
        self.damage = damage
        self.range = range

    def charge(self):
        print(f'Damage done = {self.damage}')


class Goblin(Monster):
    def __init__(self, hitpoints, damage, range, country_of_origin):
        Monster.__init__(self, hitpoints, damage, range)
        self.country_of_origin = country_of_origin
        self.__gold = 0

    def charge(self):
        print(f'Goblin is coming for you. Damage = {self.damage}')

    def steal_gold(self, how_much_gold):
        self.__gold += how_much_gold

    @property
    def gold(self):
        return self.gold


class FriendlyGoblin(Goblin):
    def __init__(self, hitpoints, damage, range, country_of_origin, fuzziness_factor):
        Goblin.__init__(self, hitpoints, damage, range, country_of_origin)
        self.fuzzy = fuzziness_factor

    # Function Overriding!!!
    def charge(self):
        print(f'Here comes a huge fuzzy hug. How fuzzy? {self.fuzzy} fuzzy...')


m1 = Monster(hitpoints=10, damage=26, range=15)
m2 = Monster(hitpoints=5, damage=10, range=100)
g1 = Goblin(hitpoints=12, damage=20, range=10, country_of_origin="England")

g1.charge()


fg1 = FriendlyGoblin(hitpoints=30,
                     damage=0,
                     range=40,
                     country_of_origin="Scottish",
                     fuzziness_factor=97)

# print(m1.range)
print(g1.range)

# print(m1.country_of_origin)
print(g1.country_of_origin)

print(fg1.fuzzy)
fg1.charge()