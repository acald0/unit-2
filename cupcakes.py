# PART 1

# class Cupcake:
#     def __init__(self, name, price, flavor, frosting, filling):
#         self.name = name
#         self.price = price
#         self.flavor = flavor
#         self.frosting = frosting
#         self.sprinkles = []
#         self.filling = filling

#     def add_sprinkles(self, *args):
#         for sprinkle in args:
#             self.sprinkles.append(sprinkle)


# my_cupcake = Cupcake("Chocolate Delight", 2.50, "Dark and milk chocolate", "Milk chocolate", "Dark chocolate")

# my_cupcake.frosting = "Dark chocolate"
# my_cupcake.filling = "Extra dark chocolate"
# my_cupcake.flavor = "Dark chocolate"
# my_cupcake.name = "Dark chocolate delight"

# my_cupcake.is_miniature = False
# print(my_cupcake.is_miniature)  

# my_cupcake.add_sprinkles("Chocolate", "Vanilla")
# print(my_cupcake.sprinkles)


# PART 2

from abc import ABC, abstractmethod


class Cupcake(ABC):
    size = "regular"
    def __init__(self, name, price, flavor, frosting, filling):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.filling = filling
        self.sprinkles = []

    def add_sprinkles(self, *args):
        for sprinkle in args:
            self.sprinkles.append(sprinkle)

    @abstractmethod
    def calculate_price(self, quantity):
        return quantity * self.price
    

class Mini(Cupcake):
    size = "mini"
    def __init__(self, name, price, flavor, frosting):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.sprinkles = []

my_mini_cupcake = Mini("Vanilla", 2.25, "Vanilla bean", "Buttercream")
print(my_mini_cupcake.name)

class Large(Cupcake):
    size = "large"
    def __init__(self, name, price, flavor, frosting):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.sprinkles = []

my_big_cupcake = Large("Raspberry", 2.75, "Raspberry vanilla", "Buttercream")
print(my_big_cupcake.size)