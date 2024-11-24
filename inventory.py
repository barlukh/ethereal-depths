""" Player inventory. Manipulates player inventory items. Also sets initial player's gold. """

import classes
import vendor

def error_gold(entity):
    """ Prints a message, if the gold amount is not sufficient for the transaction. """
    print(f"{entity} have enough gold for that transaction.")

def error_item(entity):
    """ Prints a message, if the player is trying to search for an item that doesn't exist. """
    print(f"This item is not in {entity} inventory.")

# starting amount of player's gold
player_gold = classes.Gold(100)

player_armor = {}
def buy_armor(name):
    """ Buys an Armor item from a vendor. """
    if name in vendor.vendor_armor:
        if vendor.vendor_armor[name].price <= player_gold.gold:
            player_gold.gold -= vendor.vendor_armor[name].price
            vendor.vendor_gold.gold += vendor.vendor_armor[name].price
            player_armor[name] = vendor.vendor_armor[name]
        else:
            error_gold("You don't")
    else:
        error_item("the vendor's")

def sell_armor(name):
    """ Sells an Armor item to a vendor. """
    if name in player_armor:
        if player_armor[name].price <= vendor.vendor_gold.gold:
            player_gold.gold += player_armor[name].price
            vendor.vendor_gold.gold -= player_armor[name].price
            del player_armor[name]
        else:
            error_gold("The vendor doesn't")
    else:
        error_item("your")

player_weapons = {}
def buy_weapon(name):
    """ Buys a Weapon item from a vendor. """
    if name in vendor.vendor_weapons:
        if vendor.vendor_weapons[name].price <= player_gold.gold:
            player_gold.gold -= vendor.vendor_weapons[name].price
            vendor.vendor_gold.gold += vendor.vendor_weapons[name].price
            player_weapons[name] = vendor.vendor_weapons[name]
        else:
            error_gold("You don't")
    else:
        error_item("the vendor's")

def sell_weapon(name):
    """ Sells a Weapon item to a vendor. """
    if name in player_weapons:
        if player_weapons[name].price <= vendor.vendor_gold.gold:
            player_gold.gold += player_weapons[name].price
            vendor.vendor_gold.gold -= player_weapons[name].price
            del player_weapons[name]
        else:
            error_gold("The vendor doesn't")
    else:
        error_item("your")
