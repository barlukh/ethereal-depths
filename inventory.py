""" Player inventory. Manipulates player inventory items. """

import vendor

def error(entity):
    print(f"This item is not in {entity} inventory.")

player_armor = {}
def add_armor(name):
    try:
        player_armor[name] = vendor.vendor_armor[name]
    except KeyError:
        error("the vendor's")

def remove_armor(name):
    try:
        del player_armor[name]
    except:
        error("your")

player_weapons = {}
def add_weapon(name):
    try:
        player_weapons[name] = vendor.vendor_weapons[name]
    except KeyError:
        error("the vendor's")

def remove_weapon(name):
    try:
        del player_weapons[name]
    except:
        error("your")