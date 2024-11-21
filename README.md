## About Ethereal Depths

**Work in progress.** This project is for practicing Class inheritance in Object Oriented Programming. I also tried to practice separating the code into different modules and importing the modules to different modules.


First I started with writing a module for blueprint 'classes' of different items (Armor, Weapons, ... ). This module can be built upon later (adding Potions, etc.).
This 'classes' module is then imported into the 'vendor' module. The 'vendor' module takes prewritten entries from .csv files, runs them through 'classes' and creates dictionaries for respective items.
Vendor dictionaries contain all the items given by .csv files as Class Objects, under the key of the name of the item. Dictionaries are also separated for Armor, Weapons, etc.
With this setup, the 'vendor' module serves as a shop where the player can buy items. 'Vendor' module is then imported into the 'inventory' module, which represents player inventory.
The player inventory has own dictionaries for Armor, Weapons, etc., where the player owned items are stored. It also has functions to manipulate these items (Add, Remove, ... ).
All items share the same attributes from the Item class: name, price, tier. All items inherit these attributes and add their own. Example: Weapons add their min_damage and max_damage.


Work in progress. The plan is to create a buy / sell functionality, where the player will have some gold to spend and earn. After that there should be a way to earn gold (fighting monsters). Stay tuned.
