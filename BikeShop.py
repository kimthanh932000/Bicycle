class BikeShop:
    __inventory = []
    __profit = 0

    def __init__(self, name):
        self.name = name

    def see_profit(self):
        print('Profit: ' + self.__profit)

    def add_to_inventory(self, bicycle):
        bicycle.price = bicycle.cost + bicycle.cost * 0.2
        self.__inventory.append(bicycle)

    # def get_bicycle_price(self, bicycle):
    #     return bicycle.cost * 0.2 + bicycle.cost

    def get_inventory(self):
        return self.__inventory

    def update_inventory(self, bike):
        for x in self.__inventory:
            if x.model == bike.model:
                self.__inventory.remove(x)

    def print_inventory(self):
        for item in self.__inventory:
            print('Model: ' + str(item.model) + ', weight: ' + str(item.weight) + ', cost: ' + str(item.cost))
