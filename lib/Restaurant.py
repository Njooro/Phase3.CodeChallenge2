class Restaurant:
    restaurants = []

    def __init__(self, name):
        self.name = name
        Restaurant.restaurants.append(self)

    def name(self):
        return self.name

