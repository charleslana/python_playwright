from playwright.sync_api import Page
from tests.pages.login_page import LoginPage
from ..pages.inventory_page import InventoryPage
from ..pages.cart_page import CartPage
from ..pages.checkout_page import CheckoutPage
from ..models.checkout_data import CheckoutData
from ..base_test import BaseTest


class TestCheckout(BaseTest):
    page: Page
    login: LoginPage
    inventory: InventoryPage
    cart: CartPage
    checkout: CheckoutPage

    def setup_method(self, method):
        super().setup_method(method)
        self.login = LoginPage(self.page)
        self.inventory = InventoryPage(self.page)
        self.cart = CartPage(self.page)
        self.checkout = CheckoutPage(self.page)

    def test_checkout_success(self, page):
        self.login.load()
        self.login.auto_login()

        assert self.inventory.is_loaded()
        product_name = "Sauce Labs Backpack"
        self.inventory.add_product_to_cart_by_name(product_name)
        self.inventory.assert_cart_count(1)
        self.inventory.click_cart()

        self.cart.click_checkout()

        self.checkout.fill_checkout_form()
        self.checkout.assert_checkout_overview_is_visible()
        self.checkout.click_finish()
        self.checkout.assert_checkout_complete_is_visible()

    def test_checkout_without_first_name_shows_required_field_error(self):
        self.login.load()
        self.login.auto_login()

        assert self.inventory.is_loaded()
        product_name = "Sauce Labs Backpack"
        self.inventory.add_product_to_cart_by_name(product_name)
        self.inventory.assert_cart_count(1)
        self.inventory.click_cart()

        self.cart.click_checkout()

        data = CheckoutData(first_name="", last_name="Doe", zip_code="12345")
        self.checkout.fill_checkout_form(data)

        assert self.checkout.get_error_text() == "Error: First Name is required"
