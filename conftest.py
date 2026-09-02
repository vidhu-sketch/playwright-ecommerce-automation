import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from test_data.test_data import VALID_USERNAME, VALID_PASSWORD


@pytest.fixture
def logged_in_page(page: Page):
    page.goto("https://www.saucedemo.com/")

    login_page = LoginPage(page)
    login_page.login(VALID_USERNAME, VALID_PASSWORD)

    return page


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page") or item.funcargs.get("logged_in_page")

        if page:
            page.screenshot(
                path=f"screenshots/{item.name}.png"
            )