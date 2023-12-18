class Customer:
    all_customers = []

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.reviews = []
        Customer.all_customers.append(self)

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def all(cls):
        return cls.all_customers

    def add_review(self, review):
        self.reviews.append(review)


class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self.name = name
        self.reviews = []
        Restaurant.all_restaurants.append(self)

    def __str__(self):
        return self.name

    def get_name(self):
        return self.name

    def get_reviews(self):
        return self.reviews

    def get_customers(self):
        return list(set(review.customer for review in self.reviews))

    def average_star_rating(self):
        if not self.reviews:
            return 0
        total_ratings = sum(review.rating() for review in self.reviews)
        return total_ratings / len(self.reviews)


class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating_value = rating
        self.customer.add_review(self)
        self.restaurant.reviews.append(self)
        Review.all_reviews.append(self)

    def rating(self):
        return self.rating_value

    @classmethod
    def all(cls):
        return cls.all_reviews

    def get_customer(self):
        return self.customer

    def get_restaurant(self):
        return self.restaurant


if __name__ == "__main__":
    # illustration of code 
    customer1 = Customer("Will", "Smith")
    restaurant1 = Restaurant("Qaribu Restaurant")
    review1 = Review(customer1, restaurant1, 5)

    print(customer1.full_name()) 
    print(str(Restaurant.all_restaurants[0]))  
    print(review1.rating())  
    print(Restaurant.all_restaurants[0].average_star_rating())  
