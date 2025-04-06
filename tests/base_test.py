class BaseTest:
    @classmethod
    def setup_class(cls):
        print("Setup da classe (BaseTest)")

    @classmethod
    def teardown_class(cls):
        print("Teardown da classe (BaseTest)")

    def setup_method(self, method):
        print("Setup do método (BaseTest)")

    def teardown_method(self, method):
        print("Teardown do método (BaseTest)")
