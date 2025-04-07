from typing import Optional
from playwright.sync_api import Page, expect
from ..models.checkout_data import CheckoutData
from ..components.error_box_component import ErrorBoxComponent


class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.first_name_input = page.locator("#first-name")
        self.last_name_input = page.locator("#last-name")
        self.postal_code_input = page.locator("#postal-code")
        self.continue_button = page.locator("#continue")
        self.title = page.locator("span.title[data-test='title']")
        self.finish_button = page.locator("#finish")
        self.error_box = ErrorBoxComponent(page)

    def click_checkout(self):
        pass

    def fill_checkout_form(self, data: Optional[CheckoutData] = None):
        if data is None:
            data = CheckoutData.random()

        self.first_name_input.fill(data.first_name)
        self.last_name_input.fill(data.last_name)
        self.postal_code_input.fill(data.zip_code)
        self.continue_button.click()

    def assert_checkout_overview_is_visible(self):
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text("Checkout: Overview")

    def click_finish(self):
        self.finish_button.click()

    def assert_checkout_complete_is_visible(self):
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text("Checkout: Complete!")

    def get_error_text(self) -> str:
        self.error_box.wait_until_visible()
        return self.error_box.get_text()
