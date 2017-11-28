from bicycle.BikeShop import BikeShop


class Customer:
    __lst_customer = []

    def __init__(self, name, fund, garage):
        self.name = name
        self.fund = fund
        self.garage = garage

    # add customer to list
    def add_to_lst(self, customer):
        self.__lst_customer.append(customer)

    # purchase a bike
    def purchase_bike(self, bike):
        self.garage.append(bike)
        self.fund = self.fund - bike.price
        print(str(self.name) + ' has purchased ' + str(bike.model) + ', cost ' + str(bike.price) + ', remaining fund is ' + str(self.fund) + '\n')
        # update inventory
        paw_shop = BikeShop('Paw')
        paw_shop.update_inventory(bike)

    # check if customer can buy the bike
    def isAffordable(self, bike_price, customer_fund):
        if customer_fund >= bike_price:
            return True

    # print bikes that customers can afford
    def print_affordable_bike(self, shop_inventory):
        for c in self.__lst_customer:
            print(c.name + ' can buy ', end = '')
            for bike in shop_inventory:
                if self.isAffordable(bike.price, c.fund):
                    print(bike.model, end = '| ')
            print('')

    def print_garage(self):
        print(self.name + ' owns ', end = '')
        for bike in self.garage:
            print(bike.model, end = '|')
        print('')

