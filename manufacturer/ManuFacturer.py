class Manufacturer:
    def __init__(self, name, bike_models):
        self.name = name
        self.bike_produced = bike_models

    def produce_bike(self, bike):
        self.bike_produced.append(bike)

    def sell_bike(self):
        pass
