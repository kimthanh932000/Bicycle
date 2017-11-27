from Bicycle import Bicycle
from BikeShop import BikeShop
from Customer import Customer

# create 6 bikes
abici = Bicycle('Abici', 10, 150)
bacchetta = Bicycle('Bacchetta', 5, 1000)
dahon = Bicycle('Dahon', 8, 450)
esmaltina = Bicycle('Esmaltina', 9, 500)
felt = Bicycle('Felt', 12, 250)
gazelle = Bicycle('Gazelle', 15, 300)

# create a bike shop
paw_shop = BikeShop('Paw')

# add 6 bikes to inventory
paw_shop.add_to_inventory(abici)
paw_shop.add_to_inventory(bacchetta)
paw_shop.add_to_inventory(dahon)
paw_shop.add_to_inventory(esmaltina)
paw_shop.add_to_inventory(felt)
paw_shop.add_to_inventory(gazelle)

# create 3 customers
john = Customer('John', 200, [])
mary = Customer('Mary', 500, [])
henry = Customer('Henry', 1000, [])

# add 3 customer to list
john.add_to_lst(john)
mary.add_to_lst(mary)
henry.add_to_lst(henry)

# get inventory
inventory = paw_shop.get_inventory()

# get customer list
# customers = john.get_lst_customer()

# print list of affordable bicycles
print('List of bicycles that customers can afford:')
john.print_affordable_bike(inventory)
print('')

# the initial inventory of the bike shop
print('List of bikes in inventory:')
paw_shop.print_inventory()
print('')

# purchase bike
john.purchase_bike(abici)
mary.purchase_bike(felt)
henry.purchase_bike(gazelle)
print('')

# inventory = paw_shop.get_inventory()
# for x in inventory:
#     print(x.model)

