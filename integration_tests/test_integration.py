import pytest
from ..basket import Basket
from ..product import Product
from ..discount import Discount


@pytest.fixture
def basket():
    return Basket()


def test_apply_discount_integration(basket):
    product_1 = Product("Table 1", 300, 'Made from birch. Damaged')
    product_2 = Product("Table 2", 600, 'Made from pine')

    discount_condition = lambda product: "Damaged" in product.description
    discount_amount = 50
    damaged_discount = Discount(discount_condition, discount_amount)

    basket.add_product(product_1)
    basket.add_product(product_2)

    assert basket.get_total() == 900

    damaged_discount.apply_discount(product_1)
    assert product_1.price == 250
    expected_result = """Basket:
Table 1: $250.00. Made from birch. Damaged
Table 2: $600.00. Made from pine
Total: $850.00"""

    assert str(basket) == expected_result
    assert "Table 1: $250.00" in str(basket)
    assert "Table 2: $600.00" in str(basket)