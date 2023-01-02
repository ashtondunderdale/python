import random
import numpy 

common = 1
uncommon = 2
rare = 3
superrare = 4


listOfItems = [
    ("Pistol", common, 25),
    ("SMG", uncommon, 75),
    ("Shotgun", uncommon, 75),
    ("Sniper rifle", rare, 250),
    ("AK-47", common, 50),
    ("RPG", rare, 200),
    ("Knife", superrare, 1000),
]

credits = 250
inventory = []

while True:
    print(f"1. Open crate\n2. Sell item\n3.View Inventory\n4. Add credits\n5. Quit\n\nCurrent credits: {credits}")
    choice = input("Enter your choice: ")

    if choice.isdigit():
        choice = int(choice)
        if choice in range(1, 6):

            if choice == 1:
                # opens a loot crate 
                cost = 50
                if credits < cost:
                    print("You don't have enough credits to open a crate.")
                else:
                    credits -= cost
                    item = random.choice(listOfItems)
                    print("You got a", item[0], "worth", item[2], "credits!")
                    inventory.append(item)

            elif choice == 2:
                # Sells an item from the players inventory
                if not inventory:
                    print("You don't have any items to sell.")
                else:
                    for i, item in enumerate(inventory):
                        print(i, item[0], item[2], "credits)")
                    itemIndex = input("Enter the index of the item you want to sell: ")
                    if itemIndex.isdigit():
                        itemIndex = int(itemIndex)
                        if itemIndex in range(len(inventory)):
                            item = inventory[itemIndex]
                            credits += item[2]
                            inventory.remove(item)
                            print("You sold the", item[0], "for", item[2], "credits.")
                        else:
                            print("Invalid item index.")
                    else:
                        print("Invalid input. Item index must be a number.")
                        
            elif choice == 3:
                # opens the players inventory
                if not inventory:
                    print("Your inventory is empty.")
                else:
                    for i, item in enumerate(inventory):
                        print(i, item[0], item[2], "credits)")

            elif choice == 4:
                # add credits to the player
                amount = input("Enter the amount of credits you want to get: ")
                if amount.isdigit():
                    amount = int(amount)
                    credits += amount
                    print("You got", amount, "credits.")
                else:
                    print("Invalid input. Amount of credits must be a number.")
                    
            elif choice == 5:
                print("Exiting now..")
                quit()
