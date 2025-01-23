
shopping_list = ["apples", "bananas", "carrots"]


def add_shoppinglist(new_shoppinglist): 
    shopping_list.append(new_shoppinglist)
    for item in shopping_list:
        print(item)

def remove_shoppinglist(remove_shoppinglist):
    shopping_list.remove(remove_shoppinglist)
    for item in shopping_list:
        print(item)
