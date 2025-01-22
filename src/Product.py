class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, desacription, price, quantity):
        self.name = name
        self.description = desacription
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value: int):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value

    @classmethod
    def new_product(cls, product_data):
        name = product_data.get("name")
        description = product_data.get("description")
        price = product_data.get("price")
        quantity = product_data.get("quantity")
        return cls(name, description, price, quantity)

    def __add__(self, other):
        if isinstance(other, type(self)):
            return self.__price * self.quantity + other.__price * other.quantity
        else:
            raise TypeError


class Smartphone(Product):
    def __init__(self, name, desacription, price, quantity, efficiency, model, memory, color):
        super().__init__(name, desacription, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(self, name, desacription, price, quantity, country, germination_period, color):
        super().__init__(name, desacription, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
