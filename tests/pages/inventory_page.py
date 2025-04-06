from playwright.sync_api import Page


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.inventory_container = page.locator("#inventory_container").first
        # self.inventory_container = page.locator("#inventory_container").nth(0)

    def is_loaded(self):
        return self.inventory_container.is_visible()
