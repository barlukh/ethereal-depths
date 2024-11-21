""" Classes for items. """

class Item:
    def __init__(self, name: str, price: int, tier: int):
        self.name = name
        self.price = price
        self.tier = tier
    
    def __str__(self):
        return f"This is a {self.name}. Price {self.price} gold. Tier {self.tier}."
    
    def __repr__(self):
        return f"'{self.name}', {self.price}, {self.tier}"

class Armor(Item):
    def __init__(self, name: str, price: int, tier: int, armor_rating: int):
        super().__init__(name, price, tier)
        self.armor_rating = armor_rating

    def __str__(self):
        return f"{super().__str__()} Armor Rating {self.armor_rating}."
    
    def __repr__(self):
        return f"{super().__repr__()}, {self.armor_rating}"

class Weapon(Item):
    def __init__(self, name: str, price: int, tier: int, min_dmg: int, max_dmg: int):
        super().__init__(name, price, tier)
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg

    def __str__(self):
        return f"{super().__str__()} Damage {self.min_dmg} - {self.max_dmg}."
    
    def __repr__(self):
        return f"{super().__repr__()}, {self.min_dmg}, {self.max_dmg}"