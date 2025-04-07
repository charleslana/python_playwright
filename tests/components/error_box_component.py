from playwright.sync_api import Page


class ErrorBoxComponent:
    def __init__(self, page: Page):
        self._page = page
        self._error_box = page.locator("[data-test='error']")

    def is_visible(self) -> bool:
        return self._error_box.is_visible()

    def wait_until_visible(self) -> None:
        self._error_box.wait_for(state="visible")

    def get_text(self) -> str:
        return self._error_box.text_content()
