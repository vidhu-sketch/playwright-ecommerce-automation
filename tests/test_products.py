from playwright.sync_api import Page
from pages.products_page import ProductsPage


def test_product_display(logged_in_page: Page):
    products_page = ProductsPage(logged_in_page)

    assert products_page.get_product_count() > 0


def test_add_backpack(logged_in_page: Page):
    products_page = ProductsPage(logged_in_page)
    products_page.add_backpack_to_cart()

    assert logged_in_page.locator(".shopping_cart_badge").inner_text() == "1"