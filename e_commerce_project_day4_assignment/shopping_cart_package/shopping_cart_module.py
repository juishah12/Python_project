from e_commerce_project_day4_assignment.Item_package.item_module import Item


class ShoppingCart:

    def __init__(self):
        self.type_item1 = None
        self.type_item2 = None

item1 = Item()
item2 = Item()

item1.id= "T001"
item1.descr = "Nail paint"
item1.price = 50
item1.quantity = 2

item2.id= "T002"
item2.descr = "Lipstick"
item2.price = 40
item2.quantity = 5

print(item1.descr)
print(item2.descr)

item1.discounted_price()
item2.discounted_price()
