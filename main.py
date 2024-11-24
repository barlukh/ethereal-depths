""" Main execution file for the game. """

import inventory
import vendor

def available_gold():
    """ Prints the vendor's and player's gold balance. """
    print(f"The vendor has {vendor.vendor_gold.gold} gold.")
    print(f"You have {inventory.player_gold.gold} gold.\n")

def player_input():
    """ Asks the player for an input and calls relevant functions based on the input. """
    allowed_input = [0, 1, 2, 3]
    while True:
        try:
            command = int(input("Make a choice please: "))
        except ValueError:
            print("Wrong choice, only presented numbers allowed.\n")
            continue
        if command not in allowed_input:
            print("Wrong choice, only presented numbers allowed.\n")
            continue
        elif command == 0:
            print('"Goodbye, traveler!"')
            break
        elif command == 1:
            pass
        elif command == 2:
            pass
        elif command == 3:
            available_gold()

def help():
    """ Prints available commands to the player to operate the trade interaction. """
    print("0 : Exit")
    print("1 : Buy items")
    print("2 : Sell items")
    print("3 : Available gold\n")

def trade():
    """ Starts trading with the vendor. Prints welcoming message and guides the player through the process. """
    print('"Welcome to my shop, traveler! Buying, selling, or just looking around? You won\'t find better prices anywhere else! Now, how can I help?"\n')
    help()
    player_input()

trade()