import csv
from pprint import pprint
        

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

    # @abstractmethod
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
# print(my_mini_cupcake.name)

class Large(Cupcake):
    size = "large"
    def __init__(self, name, price, flavor, frosting):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.sprinkles = []

my_big_cupcake = Large("Raspberry", 2.75, "Raspberry vanilla", "Buttercream")
# print(my_big_cupcake.size)

my_regular_cupcake = Cupcake("Chocolate Delight", 2.50, "Dark and milk chocolate", "Milk chocolate", "Dark chocolate")

another_cupcake = Large("Peanut Butter Surprise", 3, "Peanut butter", "Chocolate buttercream")

another_cupcake.add_sprinkles("Peanuts", "Chocolate")

# PART 3

def read_csv_file(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            pprint(row)

# read_csv_file("sample.csv")

cupcake_list = [
    my_mini_cupcake,
    my_regular_cupcake,
    my_big_cupcake
]

def write_new_csv(file, cupcakes):
    with open(file, "w", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "filling", "sprinkles"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for cupcake in cupcakes:
            if hasattr(cupcake, "filling"):
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "filling": cupcake.filling, "sprinkles": cupcake.sprinkles})
            else:
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles})


write_new_csv("sample.csv", cupcake_list)


def add_cupcake(file, cupcake):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "filling", "sprinkles"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if hasattr(cupcake, "filling"):
            writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "filling": cupcake.filling, "sprinkles": cupcake.sprinkles})
        else:
            writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles})

add_cupcake("sample.csv", another_cupcake)