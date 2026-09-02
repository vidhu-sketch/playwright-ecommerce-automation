from playwright.sync_api import Page
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


def test_add_product_to_cart(logged_in_page: Page):
    products_page = ProductsPage(logged_in_page)
    products_page.add_backpack_to_cart()

    cart_page = CartPage(logged_in_page)
    cart_page.open_cart()

    assert cart_page.get_cart_item_count() == 1


def test_remove_product_from_cart(logged_in_page: Page):
    products_page = ProductsPage(logged_in_page)
    products_page.add_backpack_to_cart()

    cart_page = CartPage(logged_in_page)
    cart_page.open_cart()

    cart_page.remove_backpack_from_cart()

    assert cart_page.get_cart_item_count() == 0