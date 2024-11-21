""" Reads through the .csv files with predefined items and creates respective 'vendor' dictionaries. """

import os
import csv
import classes

# default_path must be set to the directory where the .csv files are located
default_path = r"C:\Users\boris\OneDrive\Documents\Projects\ethereal_depths"
os.chdir(default_path)

vendor_armor = {}
with open("armor.csv", newline="") as file:
    csv_reader = csv.reader(file, delimiter=",")
    next(csv_reader)
    for row in csv_reader:
        vendor_armor[row[0]] = classes.Armor(row[0], int(row[1]), int(row[2]), int(row[3]))

vendor_weapons = {}
with open("weapons.csv", newline="") as file:
    csv_reader = csv.reader(file, delimiter=",")
    next(csv_reader)
    for row in csv_reader:
        vendor_weapons[row[0]] = classes.Weapon(row[0], int(row[1]), int(row[2]), int(row[3]), int(row[4]))