from playwright.sync_api import Page
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from test_data.test_data import FIRST_NAME, LAST_NAME, POSTAL_CODE


def test_complete_checkout(logged_in_page: Page):
    products_page = ProductsPage(logged_in_page)
    products_page.add_backpack_to_cart()

    cart_page = CartPage(logged_in_page)
    cart_page.open_cart()

    checkout_page = CheckoutPage(logged_in_page)
    checkout_page.start_checkout()

    checkout_page.enter_customer_details(
        first_name=FIRST_NAME,
        last_name=LAST_NAME,
        postal_code=POSTAL_CODE
    )

    checkout_page.finish_order()

    assert checkout_page.get_success_message() == "Thank you for your order!"