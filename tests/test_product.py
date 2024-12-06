import pytest

from src.Product import Product

new_product = Product.new_product(
    {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }
)

@pytest.fixture
def product1():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

@pytest.fixture
def product2():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

def test_init(product1):
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 5


def test_new_product():
    new_product.price = 0
    assert new_product.price == 180000
    new_product.price = 800
    assert new_product.price == 800

def test_sum_products(product1, product2):
    assert product1.price * product1.quantity + product2.price * product2.quantity == 2580000.0
