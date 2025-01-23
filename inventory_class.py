inventory= ["mango", "kiwi", "papaya"]

def add_inventory(new_item):
    inventory.append(new_item)
    new_item= 10


def remove_inventory(bye_item):
    inventory.remove(bye_item)
    bye_item =-3

def sinngle_item(number):
    print(inventory[number])