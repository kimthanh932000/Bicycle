from BikeShop import BikeShop


class Customer:
    __lst_customer = []

    def __init__(self, name, fund, garage):
        self.name = name
        self.fund = fund
        self.garage = garage

    def add_to_lst(self, customer):
        self.__lst_customer.append(customer)


    def purchase_bike(self, bike):
        self.garage.append(bike)
        self.fund = self.fund - bike.price
        print(str(self.name) + ' has purchased ' + str(bike.model) + ', cost ' + str(bike.price) + ', remaining fund is ' + str(self.fund))
        paw_shop = BikeShop('Paw')
        paw_shop.update_inventory(bike)

    def is_affordable(self, bike_price, customer_fund):
        if customer_fund >= bike_price:
            return True

    # bicycles that customers can afford
    def print_affordable_bike(self, shop_inventory):
        for c in self.__lst_customer:
            for bike in shop_inventory:
                if (self.is_affordable(bike.price, c.fund)):
                    print(c.name + ' can buy ' + bike.model)


