from playwright.sync_api import Page
from config import BASE_URL, USERNAME, PASSWORD
from ..components.error_box_component import ErrorBoxComponent


class LoginPage:
    def __init__(self, page: Page):
        self._page = page
        self._username_input = page.locator("#user-name")
        self._password_input = page.locator("#password")
        self._login_button = page.locator("#login-button")
        self._error_box = ErrorBoxComponent(page)

    def load(self):
        self._page.goto(f"{BASE_URL}/")

    def login(self, username: str, password: str):
        self._username_input.fill(username)
        self._password_input.fill(password)
        self._login_button.click()

    def get_error(self) -> str:
        self._error_box.wait_until_visible()
        return self._error_box.get_text()

    def auto_login(self):
        self.login(USERNAME, PASSWORD)
