from playwright.sync_api import Page


class CheckoutPage:

    def __init__(self, page: Page):
        self.page = page

        self.checkout_button = page.locator("#checkout")
        self.first_name = page.locator("#first-name")
        self.last_name = page.locator("#last-name")
        self.postal_code = page.locator("#postal-code")
        self.continue_button = page.locator("#continue")
        self.finish_button = page.locator("#finish")
        self.success_message = page.locator(".complete-header")

    def start_checkout(self):
        self.checkout_button.click()

    def enter_customer_details(self, first_name, last_name, postal_code):
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.postal_code.fill(postal_code)

    def finish_order(self):
        self.continue_button.click()
        self.finish_button.click()

    def get_success_message(self):
        return self.success_message.inner_text()