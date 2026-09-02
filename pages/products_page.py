from playwright.sync_api import Page


class ProductsPage:

    def __init__(self, page: Page):
        self.page = page

        self.products = page.locator(".inventory_item")
        self.backpack = page.locator("#add-to-cart-sauce-labs-backpack")

    def get_product_count(self):
        return self.products.count()

    def add_backpack_to_cart(self):
        self.backpack.click()