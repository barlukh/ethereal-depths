## Introduction
**Work in progress.** A game based in the classical RPG setting (armor, swords, monsters, gold and riches). There is no graphical user interface, only text-based presentation. This project is for practicing Class inheritance in Object Oriented Programming.
The focus is on separating the code into different modules and importing these modules into other modules. The main functionality is the interaction between a vendor and a player to buy and sell items. Currently working on ways to earn gold (fighting monsters).

## Functionality
- Items are manually created by the user into their respective .csv files. There are separate files for Armor, Weapons, etc. These files can be therefore manipulated externally to add or remove items from the game.
- There is a blueprint module for 'classes' of different items (Armor, Weapons, ... ). This module can be built upon later (adding Potions, etc.).
- All items share the same attributes from the Item class: name, price, tier. Items inherit these attributes and add their own. Example: Weapons add their min_damage and max_damage.
- Module 'classes' is then imported into the 'vendor' module. The 'vendor' module takes all the prewritten entries from .csv files, runs them through 'classes' and creates dictionaries for respective items.
- Vendor dictionaries contain all the items given by .csv files as Class Objects, under the key of the name of the item. Dictionaries are also separated for Armor, Weapons, etc.
- With this setup, the 'vendor' module serves as a base shop where the player can buy and sell items. 'Vendor' module is then imported into the 'inventory' module, which represents the player inventory.
- The player 'inventory' has its own dictionaries for Armor, Weapons, etc., where the player owned items are stored. It also has all the main functions to manipulate these items (buy_...() and sell_...()).
- Module 'inventory' also manipulates vendor's and player's gold according to the transaction taking place.
