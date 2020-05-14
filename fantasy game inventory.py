stuff = {'rope'     : 1,
         'torch'    : 6,
         'gold coin': 42,
         'dagger'   : 1,
         'arrow'    : 12}

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

inv = {'gold coin': 42,
       'rope'     : 1}

def addToInventory(inventory, addedItems):
    for i in range(len(addedItems)):
        if addedItems[i] in inventory.keys():
            inventory[addedItems[i]] += 1
        else:
            inventory.setdefault(addedItems[i], 1)

def displayInventory(inventory):
    print("Inventory: ")
    item_total = 0
    for k, v in inventory.items():
        item_total = item_total + v
        print(str(v) + " " + k)
    print("Total number of items: "  + str(item_total))
addToInventory(inv, dragonLoot)
displayInventory(inv)