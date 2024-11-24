class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, desacription, price, quantity):
        self.name = name
        self.description = desacription
        self.price = price
        self.quantity = quantity
