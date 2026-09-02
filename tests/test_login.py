from playwright.sync_api import Page
from pages.login_page import LoginPage
from test_data.test_data import VALID_USERNAME, VALID_PASSWORD, INVALID_PASSWORD


def test_login(page: Page):
    page.goto("https://www.saucedemo.com/")

    login_page = LoginPage(page)
    login_page.login(VALID_USERNAME, VALID_PASSWORD)

    assert page.url == "https://www.saucedemo.com/inventory.html"


def test_invalid_login(page: Page):
    page.goto("https://www.saucedemo.com/")

    login_page = LoginPage(page)
    login_page.login(VALID_USERNAME, INVALID_PASSWORD)

    assert page.locator("[data-test='error']").is_visible()