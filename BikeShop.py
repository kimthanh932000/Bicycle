class BikeShop:
    __inventory = []
    __profit = 0

    def __init__(self, name):
        self.name = name

    # add bike to inventory
    def add_to_inventory(self, bicycle):
        bicycle.price = bicycle.cost + bicycle.cost * 0.2
        self.__inventory.append(bicycle)

    # get inventory
    def get_inventory(self):
        return self.__inventory

    # update inventory
    def update_inventory(self, bike):
        for x in self.__inventory:
            if x.model == bike.model:
                self.__inventory.remove(x)
        self.update_profit(bike)

    # update profit
    def update_profit(self, bike):
        BikeShop.__profit = BikeShop.__profit + (bike.price - bike.cost)

    # print profit
    def print_profit(self):
        print('Profit: ' + str(self.__profit) + '\n')

    # print inventory
    def print_inventory(self):
        # print('List of bikes in inventory: ')
        for item in self.__inventory:
            print('Model: ' + str(item.model) + '| Weight: ' + str(item.weight) + '| Cost: ' + str(item.cost))
        print('')
