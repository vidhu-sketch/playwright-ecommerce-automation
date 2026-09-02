from playwright.sync_api import Page


class CartPage:

    def __init__(self, page: Page):
        self.page = page

        self.cart_button = page.locator(".shopping_cart_link")
        self.cart_items = page.locator(".cart_item")
        self.remove_backpack = page.locator("#remove-sauce-labs-backpack")

    def open_cart(self):
        self.cart_button.click()

    def get_cart_item_count(self):
        return self.cart_items.count()

    def remove_backpack_from_cart(self):
        self.remove_backpack.click()