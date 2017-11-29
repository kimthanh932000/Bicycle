class Bicycle:
    def __init__(self, model, wheel, frame, manufacturer):
        self.model = model
        self.weight = 2 * wheel.weight + frame.weight
        self.cost = (2 * wheel.cost + frame.cost) + (manufacturer.percentage_over_cost * (2 * wheel.cost + frame.cost))
        self.wheel = wheel
        self.frame = frame
        self.manufacturer = manufacturer

