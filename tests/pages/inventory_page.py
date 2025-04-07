from playwright.sync_api import Page


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.inventory_container = page.locator("#inventory_container").first
        # self.inventory_container = page.locator("#inventory_container").nth(0)
        self.shopping_cart = page.locator(".shopping_cart_link")

    def is_loaded(self):
        return self.inventory_container.is_visible()

    def add_product_to_cart_by_name(self, product_name: str):
        locator = self.page.locator(".inventory_item").filter(
            has=self.page.locator(f"text={product_name}")
        )
        locator.locator("button").click()

    def add_multiple_products(self, product_names: list[str]):
        for name in product_names:
            self.add_product_to_cart_by_name(name)

    def get_cart_count(self) -> int:
        link = self.shopping_cart
        if link.is_visible():
            return int(link.text_content())
        return 0

    def assert_cart_count(self, expected_count: int):
        actual_count = self.get_cart_count()
        assert (
            actual_count == expected_count
        ), f"Esperado {expected_count} itens, mas apareceu {actual_count}."

    def click_cart(self):
        self.shopping_cart.click()
