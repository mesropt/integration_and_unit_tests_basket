import pytest
from ..basket import Basket
from ..product import Product

@pytest.fixture
def basket():
    return Basket()

def test_get_total(basket):
    product_1 = Product("Table 1", 300, 'Made from birch')
    product_2 = Product("Table 2", 600, 'Made from pine')
    basket.add_product(product_1)
    basket.add_product(product_2)
    assert basket.get_total() == 900
