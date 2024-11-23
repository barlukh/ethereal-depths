""" Player inventory. Manipulates player inventory items. Also changes vendor and player gold amount. """

import classes
import vendor

def error_gold(entity):
    """ Prints a message, if the gold amount is not sufficient for the transaction. """
    print(f"{entity} have enough gold for that transaction.")

def error_item(entity):
    """ Prints a message, if the player is trying to search for an item that doesn't exist. """
    print(f"This item is not in {entity} inventory.")

def vendor_add_gold(value):
    """ Adds gold to the vendor. """
    classes.VendorGold.amount += value 

def vendor_remove_gold(value):
    """ Removes gold from the vendor. """
    classes.VendorGold.amount -= value

def player_add_gold(value):
    """ Adds gold to the player. """
    classes.PlayerGold.amount += value 

def player_remove_gold(value):
    """ Removes gold from the player. """
    classes.PlayerGold.amount -= value

player_armor = {}
def buy_armor(name):
    """ Buys an Armor item from a vendor. """
    if name in vendor.vendor_armor:
        if vendor.vendor_armor[name].price <= classes.PlayerGold.amount:
            vendor_add_gold(vendor.vendor_armor[name].price)
            player_remove_gold(vendor.vendor_armor[name].price)
            player_armor[name] = vendor.vendor_armor[name]
        else:
            error_gold("You don't")
    else:
        error_item("the vendor's")

def sell_armor(name):
    """ Sells an Armor item to a vendor. """
    if name in player_armor:
        if player_armor[name].price <= classes.VendorGold.amount:
            vendor_remove_gold(player_armor[name].price)
            player_add_gold(player_armor[name].price)
            del player_armor[name]
        else:
            error_gold("The vendor doesn't")
    else:
        error_item("your")

player_weapons = {}
def buy_weapon(name):
    """ Buys a Weapon item from a vendor. """
    if name in vendor.vendor_weapons:
        if vendor.vendor_weapons[name].price <= classes.PlayerGold.amount:
            player_weapons[name] = vendor.vendor_weapons[name]
            vendor_add_gold(vendor.vendor_weapons[name].price)
            player_remove_gold(vendor.vendor_weapons[name].price)
        else:
            error_gold("You don't")
    else:
        error_item("the vendor's")

def sell_weapon(name):
    """ Sells a Weapon item to a vendor. """
    if name in player_weapons:
        if player_weapons[name].price <= classes.VendorGold.amount:
            vendor_remove_gold(player_weapons[name].price)
            player_add_gold(player_weapons[name].price)
            del player_weapons[name]
        else:
            error_gold("The vendor doesn't")
    else:
        error_item("your")
