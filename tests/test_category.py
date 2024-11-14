import pytest

from src.Category import Category


@pytest.fixture
def category():
    return Category("Смартфоны",
                    "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                    ["one", "two", "three"])


def test_init(category):
    assert category.name == "Смартфоны"
    assert category.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    assert category.products == ["one", "two", "three"]
    assert category.category_count == 1
    assert category.product_count == 3
