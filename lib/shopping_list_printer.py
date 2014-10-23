def format_shopping_list(products):
    if(products):
        to_return = str(len(products)) + "item" + ("s" if len(products) != 1 else "") + ""
        for i in range(len(products)):
            to_return += "\n" + str(i) + ": " + str(products[i]).capitalize()
            return to_return
    else:
        return "No Items In List"