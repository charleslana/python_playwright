from playwright.sync_api import Page
from tests.pages.login_page import LoginPage
from ..pages.inventory_page import InventoryPage
from ..base_test import BaseTest


class TestInventory(BaseTest):
    page: Page
    login: LoginPage
    inventory: InventoryPage

    def setup_method(self, method):
        super().setup_method(method)
        self.login = LoginPage(self.page)
        self.inventory = InventoryPage(self.page)

    def test_add_products_to_cart(self, page):
        self.login.load()
        self.login.auto_login()

        assert self.inventory.is_loaded()

        products_to_add = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie",
        ]

        self.inventory.add_multiple_products(products_to_add)
        # self.page.wait_for_timeout(3000)
        self.inventory.assert_cart_count(len(products_to_add) + 1)
