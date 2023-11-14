class Cupcake:
    def __init__(self, name, price, flavor, frosting, filling):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.sprinkles = []
        self.filling = filling

    def add_sprinkles(self, *args):
        for sprinkle in args:
            self.sprinkles.append(sprinkle)


my_cupcake = Cupcake("Chocolate Delight", 2.50, "Dark and milk chocolate", "Milk chocolate", "Dark chocolate")

my_cupcake.frosting = "Dark chocolate"
my_cupcake.filling = "Extra dark chocolate"
my_cupcake.flavor = "Dark chocolate"
my_cupcake.name = "Dark chocolate delight"

my_cupcake.is_miniature = False
print(my_cupcake.is_miniature)  

my_cupcake.add_sprinkles("Chocolate", "Vanilla")
print(my_cupcake.sprinkles)