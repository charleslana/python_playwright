"""Testes relacionados ao processo de login da aplicação."""

from playwright.sync_api import Page
from .pages.login_page import LoginPage
from .pages.inventory_page import InventoryPage
from .utils.data_generator import get_fake_user
from .base_test import BaseTest


class TestLogin(BaseTest):
    page: Page
    login: LoginPage
    inventory: InventoryPage

    @classmethod
    def setup_class(cls):
        print("Setup antes de todos os testes da classe TestLogin")

    @classmethod
    def teardown_class(cls):
        print("Teardown depois de todos os testes da classe TestLogin")

    def setup_method(self, method):
        super().setup_method(method)
        print(f"\nSetup do teste: {method.__name__}")
        self.login = LoginPage(self.page)
        self.inventory = InventoryPage(self.page)
        # self.login = None
        # self.inventory = None

    def teardown_method(self, method):
        super().teardown_method(method)
        print(f"Teardown do teste: {method.__name__}")

    def test_successful_login(self, page):
        """Verifica se o login com credenciais válidas permite acesso à página de inventário."""
        # login = LoginPage(page)
        # inventory = InventoryPage(page)

        self.login.load()
        self.login.login("standard_user", "secret_sauce")

        assert self.inventory.is_loaded()

    def test_invalid_login(self, page):
        """
        Verifica se o sistema exibe a mensagem correta ao tentar login com credenciais inválidas
        fixas.
        """
        # login = LoginPage(page)
        self.login.load()
        self.login.login("invalid_user", "wrong_password")

        assert "Username and password do not match" in self.login.get_error()
        assert (
            self.login.get_error()
            == "Epic sadface: Username and password do not match any user in this service"
        )

    def test_login_with_invalid_credentials(self, page):
        """Verifica se o sistema exibe erro ao tentar login com dados falsos gerados pelo Faker."""
        fake_user = get_fake_user()
        # login = LoginPage(page)
        self.login.load()
        self.login.login(fake_user["username"], fake_user["password"])
        assert "Username and password do not match" in self.login.get_error()
