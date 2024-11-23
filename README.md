## Introduction
**Work in progress.** This project is for practicing Class inheritance in Object Oriented Programming. I also tried to practice separating the code into different modules and importing the modules to different modules.
The ideas was to create a shopping experience, where the game vendor has items for purchase and the player can purchase them. The plan is to create a buy / sell functionality, where the player will have some gold to spend and earn.
After that there should be a way to earn gold (fighting monsters). Stay tuned.

## Functionality
- Items are manually created by the programmer into their respective .csv files. There are separate files for Armor, Weapons, etc. These files can be therefore manipulated externally to add or remove items from the game.
- There is a blueprint module for 'classes' of different items (Armor, Weapons, ... ). This module can be built upon later (adding Potions, etc.).
- All items share the same attributes from the Item class: name, price, tier. Items inherit these attributes and add their own. Example: Weapons add their min_damage and max_damage.
- This 'classes' module is then imported into the 'vendor' module. The 'vendor' module takes all the prewritten entries from .csv files, runs them through 'classes' and creates dictionaries for respective items.
- Vendor dictionaries contain all the items given by .csv files as Class Objects, under the key of the name of the item. Dictionaries are also separated for Armor, Weapons, etc.
- With this setup, the 'vendor' module serves as a shop where the player can buy items. 'Vendor' module is then imported into the 'inventory' module, which represents the player inventory.
- The player inventory has its own dictionaries for Armor, Weapons, etc., where the player owned items are stored. It also has functions to manipulate these items (add_...(), remove_...(), ... ).
