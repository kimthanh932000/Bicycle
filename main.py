from bicycle.Bicycle import Bicycle
from bicycle.Frame import Frame
from bicycle.Wheel import Wheel
from bikeshop.BikeShop import BikeShop
from customer.Customer import Customer

# create 3 wheel types
shimano_wheel = Wheel('Shimano', 10, 30, 'wooden')
campagnolo_wheel = Wheel('Campagnolo', 5, 35, 'steel')
zipp_wheel = Wheel('Zipp', 8, 48, 'carbon')

# create 3 frames types
aluminum_frame = Frame('aluminum', 20, 100)
carbon_frame = Frame('carbon', 30, 400)
steel_frame = Frame('steel', 45, 500)

# create 6 bikes
abici = Bicycle('Abici', shimano_wheel, aluminum_frame)
bacchetta = Bicycle('Bacchetta', campagnolo_wheel, carbon_frame)
dahon = Bicycle('Dahon', zipp_wheel, steel_frame)
esmaltina = Bicycle('Esmaltina', zipp_wheel, carbon_frame)
felt = Bicycle('Felt', shimano_wheel, steel_frame )
gazelle = Bicycle('Gazelle', campagnolo_wheel, aluminum_frame)

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
print('\n**********************************\n')

# the initial inventory of the bike shop
print('The initial inventory of the bike shop:')
paw_shop.print_inventory()
print('\n**********************************\n')

# purchase bike
john.purchase_bike(abici)
print('The remaining bikes in inventory:')
paw_shop.print_inventory()
paw_shop.print_profit()
print('\n**********************************\n')

mary.purchase_bike(gazelle)
print('The remaining bikes in inventory:')
paw_shop.print_inventory()
paw_shop.print_profit()
print('\n**********************************\n')

henry.purchase_bike(dahon)
print('The remaining bikes in inventory:')
paw_shop.print_inventory()
paw_shop.print_profit()
print('\n**********************************\n')

# list of bikes that each customer owns
print('Bicycles that each customer owns:')
john.print_garage()
mary.print_garage()
henry.print_garage()