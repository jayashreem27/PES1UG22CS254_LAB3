import json

import products
from cart import dao
from products import Product


class Cart:
    def __init__(self, id: int, username: str, contents: list[Product], cost: float):
        self.id = id
        self.username = username
        self.contents = contents
        self.cost = cost

    def load(data):
        return Cart(data['id'], data['username'], data['contents'], data['cost'])


def get_cart(username: str) -> list:
    """Retrieves cart contents for a given username.

    Uses dao.get_cart_with_products to fetch products directly,
    avoiding eval and individual product lookups.

    Args:
        username: The username for which to retrieve the cart.

    Returns:
        A list of Product objects in the user's cart.
    """

    cart_products = dao.get_cart_with_products(username)
    return cart_products if cart_products is not None else []


def add_to_cart(username: str, product_id: int):
    dao.add_to_cart(username, product_id)


def remove_from_cart(username: str, product_id: int):
    dao.remove_from_cart(username, product_id)

def delete_cart(username: str):
    dao.delete_cart(username)

# No changes needed to add_to_cart, remove_from_cart, or delete_cart