import pytest

from src.Category import Category
from src.Product import Product


@pytest.fixture
def category():
    return Category("Смартфоны",
                    "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                    ["one", "two", "three"])
@pytest.fixture()
def product():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

def test_init(category):
    assert category.name == "Смартфоны"
    assert category.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    assert category.products == ["one", "two", "three"]
    assert category.category_count == 1
    assert category.product_count == 3

def test_product_list(product):
    assert f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."

