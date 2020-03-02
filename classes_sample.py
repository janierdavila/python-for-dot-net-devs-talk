class ShoppingCart:

    def __init__(self):
        self.items = []

    def addItems(self, name, price):
        self.items.append((name,price))

    def __iter__(self):
        return self.items.__iter__()

if __name__ == "__main__":
    cart = ShoppingCart()
    cart.addItems('xbox', 500)
    cart.addItems('playstation', 400)

    for item in cart:
        print(item)