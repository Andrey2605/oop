class Category:
    name: str
    description: str
    products: str

    category_count = 0
    product_count = 0

    def __init__(self, name, desacription, products):
        self.name = name
        self.description = desacription
        self.products = products


        Category.category_count += 1
        Category.product_count += len(products)
