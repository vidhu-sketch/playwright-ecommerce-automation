from pathlib import Path


def take_screenshot(page, name):
    Path("screenshots").mkdir(exist_ok=True)
    page.screenshot(path=f"screenshots/{name}.png")